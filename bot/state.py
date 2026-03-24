# Shared in-memory FSM state for session generation.
# Keys are Telegram user IDs (int).
# Values are dicts containing: state, api_id, api_hash, phone,
# client (Telethon), phone_code_hash.
#
# NOTE: This is intentionally in-memory (no persistence) per the project
# requirements — no database is used and credentials are never stored to disk.
user_states: dict[int, dict] = {}
