from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery

from helpers.keyboards import main_menu_keyboard
from helpers.messages import START_TEXT


async def start_command(client: Client, message: Message) -> None:
    await message.reply_text(
        START_TEXT,
        reply_markup=main_menu_keyboard(),
        disable_web_page_preview=True,
    )


async def back_menu_callback(client: Client, query: CallbackQuery) -> None:
    await query.message.edit_text(
        START_TEXT,
        reply_markup=main_menu_keyboard(),
        disable_web_page_preview=True,
    )
    await query.answer()


def register_start_handlers(app: Client) -> None:
    app.on_message(filters.command("start") & filters.private)(start_command)
    app.on_callback_query(filters.regex("^back_menu$"))(back_menu_callback)
