import asyncio
import logging

from pyrogram import Client

from config.config import BOT_TOKEN, API_ID, API_HASH
from bot.handlers.start import register_start_handlers
from bot.handlers.help import register_help_handlers
from bot.handlers.cancel import register_cancel_handlers
from bot.handlers.session import register_session_handlers
from bot.handlers.guides import register_guide_handlers

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


def create_app() -> Client:
    app = Client(
        name="peaky_setup_bot",
        bot_token=BOT_TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
    )
    register_start_handlers(app)
    register_help_handlers(app)
    register_cancel_handlers(app)
    register_session_handlers(app)
    register_guide_handlers(app)
    return app


async def main() -> None:
    app = create_app()
    logger.info("Starting Peaky Setup Bot…")
    async with app:
        logger.info("Bot is running. Press Ctrl+C to stop.")
        await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
