from aiogram import Dispatcher

from .throttling import ThrottlingMiddleware

def setup(dp: Dispatcher):
    dp.message.middleware(ThrottlingMiddleware())

