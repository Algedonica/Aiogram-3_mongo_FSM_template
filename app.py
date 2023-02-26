import logging
from aiohttp import web

from middlewares import ThrottlingMiddleware
from data.config import BASE_URL, OTHER_BOTS_PATH, WEB_SERVER_HOST, WEB_SERVER_PORT, MAIN_BOT_PATH

from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import (
    SimpleRequestHandler,
    TokenBasedRequestHandler,
    setup_application,
)

from loader import bot,bot_settings, storage

from handlers.users.start import main_router
from handlers.users.start_multi import form_router

async def on_startup(dispatcher: Dispatcher, bot: Bot):
    await bot.set_webhook(f"{BASE_URL}{MAIN_BOT_PATH}")
    

def main():
    logging.basicConfig(level=logging.WARNING)

    main_dispatcher = Dispatcher(storage=storage)
    main_dispatcher.include_router(main_router)
    main_dispatcher.startup.register(on_startup)
    main_dispatcher.message.middleware(ThrottlingMiddleware())

    multibot_dispatcher = Dispatcher(storage=storage)
    multibot_dispatcher.include_router(form_router)
    multibot_dispatcher.message.middleware(ThrottlingMiddleware())


    app = web.Application()
    SimpleRequestHandler(dispatcher=main_dispatcher, bot=bot).register(app, path=MAIN_BOT_PATH)
    TokenBasedRequestHandler(
        dispatcher=multibot_dispatcher,
        bot_settings=bot_settings,
    ).register(app, path=OTHER_BOTS_PATH)

    setup_application(app, main_dispatcher, bot=bot)
    setup_application(app, multibot_dispatcher)



    web.run_app(app, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT)


if __name__ == "__main__":
    main()
