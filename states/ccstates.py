from aiogram.filters import state
from aiogram.fsm.state import StatesGroup,State

class ProjectManage(StatesGroup):
    menu = State()
class SupportManage(StatesGroup):
    menu = State()
class SetupBTSstates(StatesGroup):
    getadmincode = State()
    catchadmincode = State()
