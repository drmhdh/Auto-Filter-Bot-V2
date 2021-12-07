import re
import base64
import logging
from struct import pack
from pyrogram.types import Message
from typing import List
from datetime import datetime
from typing import Union

from pyrogram.errors import InputUserDeactivated, UserNotParticipant, FloodWait, UserIsBlocked, PeerIdInvalid
from info import AUTH_CHANNEL, AUTH_USERS, AUTH_GROUPS, BUTTON, START_MSG, CHANNELS, ADMINS, PICS, API_KEY
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.file_id import FileId
from pymongo.errors import DuplicateKeyError
from umongo import Instance, Document, fields

from marshmallow.exceptions import ValidationError
import os


import json
from info import AUTH_CHANNEL, API_KEY

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


















         
            
        



async def is_subscribed(bot, query):
    try:
        user = await bot.get_chat_member(AUTH_CHANNEL, query.from_user.id)
    except UserNotParticipant:
        pass
    except Exception as e:
        logger.exception(e)
    else:
        if not user.status == 'kicked':
            return True

    return False

