import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
# API_ID / API_HASH for the bot's own Pyrogram client.
# You can get these from https://my.telegram.org — any valid app credentials work.
API_ID = int(os.environ.get("API_ID", 6))
API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")

if not BOT_TOKEN:
    raise ValueError(
        "BOT_TOKEN environment variable is not set. "
        "Please set it before running the bot."
    )
