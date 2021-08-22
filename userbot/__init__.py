import ast
import logging
import os
from configparser import ConfigParser
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from userbot.userbot import UserBot

# Created logs folder if it is not there. Needed for logging.
if not os.path.exists('logs'):
    os.makedirs('logs')

# Logging at the start to catch everything
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.WARNING,
    handlers=[
        TimedRotatingFileHandler(
            "logs/userbot.log",
            when="midnight",
            encoding=None,
            delay=False,
            backupCount=10,
        ),
        logging.StreamHandler(),
    ],
)
LOGS = logging.getLogger(__name__)

# Extra details
__version__ = "0.1.0"
__author__ = "soukron"

UserBot = UserBot(__version__)

# Read from config file
config_file = 'userbot.ini'
config = ConfigParser()
config.read(config_file)

# MongoDB details
MONGO_URL = config.get("mongo", "url")
DB_NAME = config.get("mongo", "db_name", fallback="userbot")
DB_USERNAME = config.get("mongo", "db_username")
DB_PASSWORD = config.get("mongo", "db_password")
IS_ATLAS = config.getboolean("mongo", "is_atlas", fallback=False)

# Other Users
ALLOWED_USERS = ast.literal_eval(
    config.get("users", "allowed_users", fallback="[]")
)

# MISC APIs
YOURLS_URL = config.get("misc", "yourls_url", fallback=None)
YOURLS_KEY = config.get("misc", "yourls_key", fallback=None)

# Get the Values from our .env
LOG_GROUP = config.get("logs", "log_group")

# Anime downloader
ANIME_DOWNLOADS_DIR = config.get("anime", "downloads_dir", fallback="downloads")

# Scheduler
scheduler = AsyncIOScheduler()

# Global Variables
CMD_HELP = {}
client = None
START_TIME = datetime.now()
