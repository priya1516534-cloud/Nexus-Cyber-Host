import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "Nexus@123")
PORT = int(os.getenv("PORT", 10000))
