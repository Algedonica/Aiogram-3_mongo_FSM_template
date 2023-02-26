
from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states.ccstates import ProjectManage
from typing import Any, Dict, Union

form_router = Router()



# @form_router.message(Command(commands=["dsd"]))
# async def dsdaasdsa(message: Message, command: CommandObject, bot: Bot) -> Any:
#     return await message.answer(f"uccessрорful added")


@form_router.message(Command(commands=["dsd"]))
async def dsdadaa(message: Message, command: CommandObject, state:FSMContext) -> Any:
    await state.set_state(ProjectManage.menu)
    await state.set_data(data={"ds":"dsa"})
    bdsad=await state.get_state()
    await state.update_data(data={"ds":"dsa"})
    # print(bdsad)
    return await message.answer(f"uccessful added")