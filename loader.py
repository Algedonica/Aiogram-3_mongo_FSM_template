from aiogram import Bot
from aiogram.client.session.aiohttp import AiohttpSession
from data.config import states_connect
from utils import mongo
from aiogram.fsm.storage.base import  StorageKey
from os import getenv
from aiogram.utils.token import TokenValidationError, validate_token
from typing import Any, Dict, Union
from data.config import OTHER_BOTS_PATH, MAIN_BOT_TOKEN


def is_bot_token(value: str) -> Union[bool, Dict[str, Any]]:
    try:
        validate_token(value)
    except TokenValidationError:
        return False
    return True


session = AiohttpSession()
bot_settings = {"session": session, "parse_mode": "HTML"}

bot = Bot(token=MAIN_BOT_TOKEN, **bot_settings)

storage = mongo.MongoStorage(uri=states_connect,
                           database='FSM_states',
                           collection_states='states'
                           )

