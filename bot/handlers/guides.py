from pyrogram import Client, filters
from pyrogram.types import CallbackQuery

from helpers.keyboards import back_to_menu_keyboard
from helpers.messages import GUIDE_API_TEXT, GUIDE_TOKEN_TEXT


async def guide_api_callback(client: Client, query: CallbackQuery) -> None:
    await query.message.edit_text(
        GUIDE_API_TEXT,
        reply_markup=back_to_menu_keyboard(),
        disable_web_page_preview=True,
    )
    await query.answer()


async def guide_token_callback(client: Client, query: CallbackQuery) -> None:
    await query.message.edit_text(
        GUIDE_TOKEN_TEXT,
        reply_markup=back_to_menu_keyboard(),
        disable_web_page_preview=True,
    )
    await query.answer()


def register_guide_handlers(app: Client) -> None:
    app.on_callback_query(filters.regex("^guide_api$"))(guide_api_callback)
    app.on_callback_query(filters.regex("^guide_token$"))(guide_token_callback)
