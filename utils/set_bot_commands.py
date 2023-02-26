from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand(command="start", description="Launch the work"),
        types.BotCommand(command="menu", description="Open main menu"),
        types.BotCommand(command="lang", description="Language switch (only in menu)")
    ])