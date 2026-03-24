from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🔑 Generate String Session", callback_data="gen_session"
                )
            ],
            [
                InlineKeyboardButton(
                    "📘 How to Get API ID & HASH", callback_data="guide_api"
                )
            ],
            [
                InlineKeyboardButton(
                    "🤖 How to Create Bot Token", callback_data="guide_token"
                )
            ],
            [
                InlineKeyboardButton("❓ Help", callback_data="help"),
                InlineKeyboardButton(
                    "📢 Join Channel", url="https://t.me/eSportLeaker"
                ),
            ],
        ]
    )


def cancel_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton("❌ Cancel", callback_data="cancel")]]
    )


def back_to_menu_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton("🏠 Back to Menu", callback_data="back_menu")]]
    )
