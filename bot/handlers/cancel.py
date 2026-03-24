from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery

from helpers.keyboards import main_menu_keyboard
from helpers.messages import CANCELLED_TEXT

from bot.state import user_states
from bot.handlers.session import cleanup_client


async def cancel_command(client: Client, message: Message) -> None:
    user_id = message.from_user.id
    await _do_cancel(client, user_id)
    await message.reply_text(
        CANCELLED_TEXT,
        reply_markup=main_menu_keyboard(),
    )


async def cancel_callback(client: Client, query: CallbackQuery) -> None:
    user_id = query.from_user.id
    await _do_cancel(client, user_id)
    await query.message.edit_text(
        CANCELLED_TEXT,
        reply_markup=main_menu_keyboard(),
    )
    await query.answer("Cancelled.")


async def _do_cancel(client: Client, user_id: int) -> None:
    if user_id in user_states:
        await cleanup_client(user_id)


def register_cancel_handlers(app: Client) -> None:
    app.on_message(filters.command("cancel") & filters.private)(cancel_command)
    app.on_callback_query(filters.regex("^cancel$"))(cancel_callback)
