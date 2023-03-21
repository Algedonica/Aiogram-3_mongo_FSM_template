from motor.motor_asyncio import AsyncIOMotorClient
from aiogram.fsm.storage.base import BaseStorage, StorageKey, StateType
from aiogram.fsm.state import State
from aiogram import Bot

from typing import Any, Dict, Optional, Union


class MongoStorage(BaseStorage):
    def __init__(self, uri: str, database: str, collection_states: str) -> None:
        self.client = AsyncIOMotorClient(uri)
        self.db = self.client[database]
        self.collection = self.db[collection_states]

    async def set_state(self, bot: Bot, key: StorageKey, state: StateType = None) -> None:
        data = await self.get_data(bot, key)
        data['state'] = state
        final_state=resolve_state(data['state'])
        await self.collection.update_one({'key': key.__dict__}, {'$set': {"state":final_state}}, upsert=True)


    async def get_state(self, bot: Bot, key: StorageKey) -> Optional[str]:
        data = await self.collection.find_one({'key': key.__dict__})
        if data:
            return data.get('state')
        return None

    async def set_data(self, bot: Bot, key: StorageKey, data: Dict[str, Any]) -> None:
        await self.collection.update_one({'key': key.__dict__}, {'$set': {"data":data}}, upsert=True)

    async def get_data(self, bot: Bot, key: StorageKey) -> Dict[str, Any]:
        data = await self.collection.find_one({'key': key.__dict__})
        if data :
            return data
        else:
            return {}

    async def update_data(
        self, bot: Bot, key: StorageKey, data: Optional[Dict[str, Any]] = None, **kwargs: Any
    ) -> Dict[str, Any]:
        if data:
            kwargs.update(data)
        await self.collection.update_one({'key': key.__dict__}, {'$set': {"data":kwargs}}, upsert=True)
        return kwargs

    async def close(self) -> None:  # pragma: no cover
        """
        Close storage (database connection, file or etc.)
        """
        pass

    # async def clear(self) -> None:
    #     await self.set_state(state=None)
    #     await self.set_data({})



def resolve_state(value):
    if isinstance(value, State):
        return value.state
    if value is None:
        return
    if value is str:
        return value



# state.key = StorageKey(bot_id=botid, chat_id=chat_id, user_id=userid, destiny='default')