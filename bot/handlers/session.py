import logging

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, Message
from telethon import TelegramClient
from telethon.errors import (
    ApiIdInvalidError,
    FloodWaitError,
    PasswordHashInvalidError,
    PhoneCodeEmptyError,
    PhoneCodeExpiredError,
    PhoneCodeHashEmptyError,
    PhoneCodeInvalidError,
    PhoneNumberBannedError,
    PhoneNumberInvalidError,
    SessionPasswordNeededError,
)
from telethon.sessions import StringSession

from helpers.keyboards import back_to_menu_keyboard, cancel_keyboard
from helpers.messages import (
    ASK_API_HASH_TEXT,
    ASK_API_ID_TEXT,
    ASK_OTP_TEXT,
    ASK_PASSWORD_TEXT,
    ASK_PHONE_TEXT,
    ERROR_TEXT,
    INVALID_API_ID_TEXT,
    SESSION_SUCCESS_TEXT,
)

logger = logging.getLogger(__name__)

from bot.state import user_states

# ── FSM state constants ────────────────────────────────────────────────────────
STATE_API_ID = "waiting_api_id"
STATE_API_HASH = "waiting_api_hash"
STATE_PHONE = "waiting_phone"
STATE_OTP = "waiting_otp"
STATE_PASSWORD = "waiting_password"


# ── Helpers ────────────────────────────────────────────────────────────────────

async def cleanup_client(user_id: int) -> None:
    """Disconnect the Telethon client and remove all state for a user."""
    data = user_states.pop(user_id, None)
    if data:
        tg_client: TelegramClient | None = data.get("client")
        if tg_client and tg_client.is_connected():
            try:
                await tg_client.disconnect()
            except Exception:
                pass


async def _safe_delete(message: Message) -> None:
    """Try to delete a message silently (best-effort)."""
    try:
        await message.delete()
    except Exception:
        pass


# ── Entry point callback ───────────────────────────────────────────────────────

async def gen_session_callback(client: Client, query: CallbackQuery) -> None:
    user_id = query.from_user.id
    # Clear any stale state
    await cleanup_client(user_id)
    user_states[user_id] = {"state": STATE_API_ID}

    await query.message.edit_text(
        ASK_API_ID_TEXT,
        reply_markup=cancel_keyboard(),
    )
    await query.answer()


# ── Message router ─────────────────────────────────────────────────────────────

async def session_message_handler(client: Client, message: Message) -> None:
    user_id = message.from_user.id
    data = user_states.get(user_id)

    if not data:
        # User is not in a session generation flow — ignore
        return

    state = data.get("state")

    if state == STATE_API_ID:
        await handle_api_id(client, message, data)
    elif state == STATE_API_HASH:
        await handle_api_hash(client, message, data)
    elif state == STATE_PHONE:
        await handle_phone(client, message, data)
    elif state == STATE_OTP:
        await handle_otp(client, message, data)
    elif state == STATE_PASSWORD:
        await handle_password(client, message, data)


# ── Step handlers ──────────────────────────────────────────────────────────────

async def handle_api_id(client: Client, message: Message, data: dict) -> None:
    text = message.text.strip() if message.text else ""
    await _safe_delete(message)

    if not text.isdigit():
        await client.send_message(
            message.chat.id,
            INVALID_API_ID_TEXT,
            reply_markup=cancel_keyboard(),
        )
        return

    data["api_id"] = int(text)
    data["state"] = STATE_API_HASH

    await client.send_message(
        message.chat.id,
        ASK_API_HASH_TEXT,
        reply_markup=cancel_keyboard(),
    )


async def handle_api_hash(client: Client, message: Message, data: dict) -> None:
    text = message.text.strip() if message.text else ""
    await _safe_delete(message)

    data["api_hash"] = text
    data["state"] = STATE_PHONE

    await client.send_message(
        message.chat.id,
        ASK_PHONE_TEXT,
        reply_markup=cancel_keyboard(),
    )


async def handle_phone(client: Client, message: Message, data: dict) -> None:
    phone = message.text.strip() if message.text else ""
    await _safe_delete(message)

    api_id: int = data["api_id"]
    api_hash: str = data["api_hash"]

    # Create a fresh Telethon client with a blank StringSession
    tg_client = TelegramClient(StringSession(), api_id, api_hash)

    try:
        await tg_client.connect()
        result = await tg_client.send_code_request(phone)
    except PhoneNumberInvalidError:
        await tg_client.disconnect()
        await client.send_message(
            message.chat.id,
            ERROR_TEXT.format(error="Invalid phone number. Please include country code (e.g. +91...)."),
            reply_markup=cancel_keyboard(),
        )
        return
    except PhoneNumberBannedError:
        await tg_client.disconnect()
        await client.send_message(
            message.chat.id,
            ERROR_TEXT.format(error="This phone number is banned from Telegram."),
            reply_markup=cancel_keyboard(),
        )
        return
    except ApiIdInvalidError:
        await tg_client.disconnect()
        await cleanup_client(message.from_user.id)
        await client.send_message(
            message.chat.id,
            ERROR_TEXT.format(error="Invalid API ID or API HASH. Please start over with /start."),
            reply_markup=back_to_menu_keyboard(),
        )
        return
    except FloodWaitError as e:
        await tg_client.disconnect()
        await client.send_message(
            message.chat.id,
            ERROR_TEXT.format(error=f"Too many requests. Please wait {e.seconds} seconds and try again."),
            reply_markup=cancel_keyboard(),
        )
        return
    except Exception as e:
        await tg_client.disconnect()
        logger.exception("Error sending code request")
        await client.send_message(
            message.chat.id,
            ERROR_TEXT.format(error=str(e)),
            reply_markup=cancel_keyboard(),
        )
        return

    data["phone"] = phone
    data["client"] = tg_client
    data["phone_code_hash"] = result.phone_code_hash
    data["state"] = STATE_OTP

    await client.send_message(
        message.chat.id,
        ASK_OTP_TEXT,
        reply_markup=cancel_keyboard(),
    )


async def handle_otp(client: Client, message: Message, data: dict) -> None:
    code = message.text.strip() if message.text else ""
    await _safe_delete(message)

    tg_client: TelegramClient = data["client"]
    phone: str = data["phone"]
    phone_code_hash: str = data["phone_code_hash"]
    user_id = message.from_user.id

    try:
        await tg_client.sign_in(
            phone=phone,
            code=code,
            phone_code_hash=phone_code_hash,
        )
    except SessionPasswordNeededError:
        data["state"] = STATE_PASSWORD
        await client.send_message(
            message.chat.id,
            ASK_PASSWORD_TEXT,
            reply_markup=cancel_keyboard(),
        )
        return
    except (PhoneCodeInvalidError, PhoneCodeEmptyError):
        await client.send_message(
            message.chat.id,
            ERROR_TEXT.format(error="Invalid OTP. Please check the code and try again."),
            reply_markup=cancel_keyboard(),
        )
        return
    except PhoneCodeExpiredError:
        await cleanup_client(user_id)
        await client.send_message(
            message.chat.id,
            ERROR_TEXT.format(error="OTP expired. Please use /start to begin again."),
            reply_markup=back_to_menu_keyboard(),
        )
        return
    except PhoneCodeHashEmptyError as e:
        logger.exception("Empty phone code hash during sign-in")
        await cleanup_client(user_id)
        await client.send_message(
            message.chat.id,
            ERROR_TEXT.format(error=str(e)),
            reply_markup=back_to_menu_keyboard(),
        )
        return
    except Exception as e:
        logger.exception("Unexpected error during sign-in")
        await cleanup_client(user_id)
        await client.send_message(
            message.chat.id,
            ERROR_TEXT.format(error=str(e)),
            reply_markup=back_to_menu_keyboard(),
        )
        return

    await _finish_session(client, message.chat.id, tg_client, user_id)


async def handle_password(client: Client, message: Message, data: dict) -> None:
    password = message.text.strip() if message.text else ""
    await _safe_delete(message)

    tg_client: TelegramClient = data["client"]
    user_id = message.from_user.id

    try:
        await tg_client.sign_in(password=password)
    except PasswordHashInvalidError:
        await client.send_message(
            message.chat.id,
            ERROR_TEXT.format(error="Incorrect 2FA password. Please try again."),
            reply_markup=cancel_keyboard(),
        )
        return
    except Exception as e:
        logger.exception("Error during 2FA sign-in")
        await cleanup_client(user_id)
        await client.send_message(
            message.chat.id,
            ERROR_TEXT.format(error=str(e)),
            reply_markup=back_to_menu_keyboard(),
        )
        return

    await _finish_session(client, message.chat.id, tg_client, user_id)


async def _finish_session(
    client: Client, chat_id: int, tg_client: TelegramClient, user_id: int
) -> None:
    """Extract the string session, send it to the user, and clean up."""
    try:
        session_string = tg_client.session.save()
    except Exception as e:
        logger.exception("Error saving session")
        await cleanup_client(user_id)
        await client.send_message(
            chat_id,
            ERROR_TEXT.format(error=str(e)),
            reply_markup=back_to_menu_keyboard(),
        )
        return

    await cleanup_client(user_id)

    await client.send_message(
        chat_id,
        SESSION_SUCCESS_TEXT.format(session=session_string),
        reply_markup=back_to_menu_keyboard(),
    )


# ── Registration ───────────────────────────────────────────────────────────────

def register_session_handlers(app: Client) -> None:
    app.on_callback_query(filters.regex("^gen_session$"))(gen_session_callback)
    app.on_message(filters.private & filters.text & ~filters.command(["start", "help", "cancel"]))(
        session_message_handler
    )
