START_TEXT = """
👋 **Welcome to Peaky Setup Bot!**

I'm your all-in-one assistant for setting up Telegram bots. I can help you:

🔑 **Generate a Pyrogram String Session**
📘 **Get your API ID & API HASH**
🤖 **Create a Bot Token**

Choose an option below to get started! 👇
"""

HELP_TEXT = """
❓ **Help — Peaky Setup Bot**

**Available Commands:**
• `/start` — Show the main menu
• `/help` — Show this help message
• `/cancel` — Cancel the current operation

**How it works:**
1. Click **Generate String Session** to start the wizard
2. You'll be asked for your **API ID**, **API HASH**, and **phone number**
3. Enter the **OTP** you receive on Telegram
4. Your **String Session** will be sent to you privately

**Need guidance?** Use the buttons to learn how to get your API credentials or create a bot token.

⚠️ **Privacy:** Your credentials are never stored. All data is discarded after the session is generated.

👨‍💻 **Developer:** Satyam Xd
📢 **Channel:** [eSportLeaker](https://t.me/eSportLeaker)
"""

CANCELLED_TEXT = """
❌ **Operation Cancelled**

The current operation has been cancelled. Your data has been cleared.

Use /start to go back to the main menu.
"""

ASK_API_ID_TEXT = """
🔑 **Step 1 of 3 — Enter Your API ID**

Please send your **API ID** (a number).

👉 Don't have one? Click ❌ Cancel and use the **"How to Get API ID & HASH"** guide first.
"""

ASK_API_HASH_TEXT = """
🔐 **Step 2 of 3 — Enter Your API HASH**

Please send your **API HASH** (a long hex string).
"""

ASK_PHONE_TEXT = """
📱 **Step 3 of 3 — Enter Your Phone Number**

Please send your **phone number with country code**.

Example: `+919876543210`

⚠️ This is used only to send the OTP. It will not be stored.
"""

ASK_OTP_TEXT = """
✅ **OTP Sent!**

A verification code has been sent to your Telegram account.

Please enter the **OTP** you received.

💡 **Tip:** Enter the code exactly as received (e.g. `12345`).
"""

ASK_PASSWORD_TEXT = """
🔒 **Two-Factor Authentication Detected**

Your account has 2FA (Two-Step Verification) enabled.

Please enter your **2FA password** to continue.
"""

SESSION_SUCCESS_TEXT = """
🎉 **String Session Generated Successfully!**

Your **Pyrogram String Session** is below. Keep it **safe and private**!

```
{session}
```

⚠️ **WARNING:**
• Never share this session with anyone
• Anyone with this session can access your account
• Store it securely (e.g. as an environment variable)

✅ All your temporary data has been cleared.
"""

INVALID_API_ID_TEXT = """
❌ **Invalid API ID**

The API ID must be a **number** (e.g. `12345678`).

Please send a valid API ID, or press Cancel.
"""

GUIDE_API_TEXT = """
📘 **How to Get API ID & API HASH**

Follow these steps:

1️⃣ Go to [my.telegram.org](https://my.telegram.org)
2️⃣ Log in with your phone number
3️⃣ Click on **"API development tools"**
4️⃣ Fill in the form:
   • **App title:** Any name (e.g. `MyApp`)
   • **Short name:** Any short name (e.g. `myapp`)
5️⃣ Click **"Create application"**
6️⃣ Copy your **App api_id** and **App api_hash**

✅ That's it! Now come back and use **Generate String Session**.
"""

GUIDE_TOKEN_TEXT = """
🤖 **How to Create a Bot Token**

Follow these steps:

1️⃣ Open Telegram and search for **@BotFather**
2️⃣ Start the bot and send `/newbot`
3️⃣ Enter a **name** for your bot (e.g. `My Music Bot`)
4️⃣ Enter a **username** for your bot (must end in `bot`, e.g. `mymusicbot`)
5️⃣ BotFather will send you a **token** that looks like:
   `123456789:ABCdef...`

✅ Copy and save that token — it's your **BOT_TOKEN**!

⚠️ Never share your bot token with anyone.
"""

ERROR_TEXT = """
⚠️ **Something went wrong**

An error occurred: `{error}`

Please try again or use /cancel to restart.
"""
