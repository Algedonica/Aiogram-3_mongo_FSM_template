from aiogram.filters.callback_data import CallbackData

class CallBackBase(CallbackData,prefix="ticket_call"):
    param1: str
    param2: str
