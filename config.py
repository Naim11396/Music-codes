from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "")
API_ID = int(getenv("API_ID", "27305765"))
API_HASH = getenv("API_HASH", "c3d9e1be50a6777fae7fadd3f156e15a")
BOT_TOKEN = getenv("BOT_TOKEN", "8094349979:AAGxJ29LU8fuUN6pJFHqiIiiMK8ZU8JburU")
BOT_NAME = getenv("BOT_NAME", "Music Bot") 
BOT_USERNAME = getenv("BOT_USERNAME", "@mustimuzik_bot")
BOT_CHANNEL = getenv("BOT_CHANNEL", "")
ASS_USERNAME = getenv("ASS_USERNAME", "")
OWNER = getenv("OWNER", "7194000526")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", 500))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6181368568").split()))
