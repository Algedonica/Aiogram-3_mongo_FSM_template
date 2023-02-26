import imp
from pymongo import settings
from data.config import staff_collection
from loader import dp, bot
from datetime import datetime
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, user, KeyboardButton, ReplyKeyboardMarkup

import secrets

def issupport(x):
    thisuser=staff_collection.find({"user_id":x, "$or":[{"staffrole":"support"},{"staffrole":"owner"}, {"staffrole":"admin"}]})
    if thisuser.count()==1:
        return True      
    else:
        return False
def isowner(x):
    thisuser=staff_collection.find({"user_id":x, "$or":[{"staffrole":"owner"}]})
    if thisuser.count()==1:
        return True      
    else:
        return False
def isadmin(x):
    thisuser=staff_collection.find({"user_id":x, "$or":[{"staffrole":"owner"},{"staffrole":"admin"}]})
    if thisuser.count()==1:
        return True      
    else:
        return False


            
def support_role_check(x):
    thisuser=staff_collection.find_one({"user_id":x})
    if thisuser["role"]=="1":
        return 'MAIN'      
    else:
        return 'PLUS'

def reverse_check(x):
    thisuser=staff_collection.find_one({"user_id":x})
    if thisuser!=None:
        if thisuser["isreverse"]==True:
            return False      
        else:
            return True
    else:
        return True

def xstr(s):
    if s is None:
        return 'none'
    return str(s)

