
from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states.ccstates import ProjectManage
from typing import Any, Dict, Union

from aiogram.utils.token import TokenValidationError, validate_token
from aiogram.exceptions import TelegramUnauthorizedError
from data.config import OTHER_BOTS_URL


main_router = Router()



@main_router.message(Command(commands=["dsd"]))
async def dsdadaa(message: Message, command: CommandObject, state:FSMContext) -> Any:
    await state.set_state(ProjectManage.menu)
    await state.set_data(data={"ds":"dsa"})
    bdsad=await state.get_state()
    await state.update_data(data={"ds":"dsa"})
    # print(bdsad)
    return await message.answer(f"uccessful added")






def is_bot_token(value: str) -> Union[bool, Dict[str, Any]]:
    try:
        validate_token(value)
    except TokenValidationError:
        return False
    return True
@main_router.message(Command(commands=["add"], magic=F.args.func(is_bot_token)))
async def command_add_bot(message: Message, command: CommandObject, bot: Bot) -> Any:
    new_bot = Bot(token=str(command.args), session=bot.session)
    try:
        bot_user = await new_bot.get_me()
    except TelegramUnauthorizedError:
        return message.answer("Invalid token")
    await new_bot.delete_webhook(drop_pending_updates=True)
    await new_bot.set_webhook(OTHER_BOTS_URL.format(bot_token=command.args))
    return await message.answer(f"Bot @{bot_user.username} successful added")