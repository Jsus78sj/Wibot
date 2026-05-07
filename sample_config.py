import os

from dotenv import load_dotenv

load_dotenv(
    "config.env" if os.path.isfile("config.env") else "sample_config.env"
)


def _int_env(key, default=None):
    val = os.environ.get(key)
    if val is None or val == "":
        if default is None:
            return 0
        return default
    return int(val)


BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = _int_env("API_ID", 0)
SESSION_STRING = os.environ.get("SESSION_STRING", "")
API_HASH = os.environ.get("API_HASH", "")
USERBOT_PREFIX = os.environ.get("USERBOT_PREFIX", "\\")
PHONE_NUMBER = os.environ.get("PHONE_NUMBER", "")
SUDO_USERS_ID = list(
    map(int, [x for x in os.environ.get("SUDO_USERS_ID", "").split() if x])
)
LOG_GROUP_ID = _int_env("LOG_GROUP_ID", 0)
GBAN_LOG_GROUP_ID = _int_env("GBAN_LOG_GROUP_ID", 0)
MESSAGE_DUMP_CHAT = _int_env("MESSAGE_DUMP_CHAT", 0)
WELCOME_DELAY_KICK_SEC = _int_env("WELCOME_DELAY_KICK_SEC", 600)
MONGO_URL = os.environ.get("MONGO_URL", "mongodb://localhost:27017")
ARQ_API_KEY = os.environ.get("ARQ_API_KEY", "")
ARQ_API_URL = os.environ.get("ARQ_API_URL", "https://thearq.tech")
LOG_MENTIONS = os.environ.get("LOG_MENTIONS", "True").lower() in ["true", "1"]
RSS_DELAY = _int_env("RSS_DELAY", 300)
PM_PERMIT = os.environ.get("PM_PERMIT", "False").lower() in ["true", "1"]
