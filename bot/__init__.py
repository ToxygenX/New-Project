import asyncio
import glob
import logging
import os
import sys
import time
from distutils.util import strtobool as sb
from logging import DEBUG, WARNING, basicConfig, getLogger, INFO
from logging.handlers import RotatingFileHandler
from pathlib import Path
from sys import argv
from telethon import TelegramClient, events, functions, types
import telethon.utils

ENV = os.environ.get("ENV", False)
if ENV:
    from bot.Config import Config
else:
    from local_config import Development as Config

    
# starting the client
bot = TelegramClient("botx", api_id=Config.API_ID, api_hash=Config.API_HASH)

# checking necessary vars
ENV = os.environ.get("ENV", False)
if bool(ENV):
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

    if CONSOLE_LOGGER_VERBOSE:
        basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=DEBUG,
        )
    else:
        basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=INFO
        )
    logger = getLogger(__name__)
    
if Config.BOT_TOKEN is None:
    logger.info("BOT_TOKEN is None. Bot Is Quiting...")
    sys.exit(1)
if Config.API_ID is None:
    logger.info("API_ID Is None.")
    sys.exit(1)
if Config.API_HASH is None:
    logger.info("API_HASH Is None. Exiting...")
    sys.exit(1)
if Config.OWNER_ID is None:
    logger.info("OWNER_ID is None. Please Add Your ID to Continue.")
    sys.exit(1)
