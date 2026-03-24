from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery

from helpers.keyboards import back_to_menu_keyboard
from helpers.messages import HELP_TEXT


async def help_command(client: Client, message: Message) -> None:
    await message.reply_text(
        HELP_TEXT,
        reply_markup=back_to_menu_keyboard(),
        disable_web_page_preview=True,
    )


async def help_callback(client: Client, query: CallbackQuery) -> None:
    await query.message.edit_text(
        HELP_TEXT,
        reply_markup=back_to_menu_keyboard(),
        disable_web_page_preview=True,
    )
    await query.answer()


def register_help_handlers(app: Client) -> None:
    app.on_message(filters.command("help") & filters.private)(help_command)
    app.on_callback_query(filters.regex("^help$"))(help_callback)
