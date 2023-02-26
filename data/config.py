import os
from dotenv import load_dotenv
import pymongo
load_dotenv()


client = pymongo.MongoClient(str(os.getenv("db_connect")))
states_connect=str(os.getenv("states_connect"))

db = client.s4bot

settings_collection = db.settings
bots_collection=db.bots

settings_obj=settings_collection.find_one({"check":"this"})



MAIN_BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

MAIN_BOT_PATH = str(os.getenv("MAIN_BOT_PATH"))

BASE_URL = str(os.getenv("BASE_URL"))
if bool(os.getenv("TESTON"))==True:
    BASE_URL = str(os.getenv("TEST_URL"))

OTHER_BOTS_PATH = str(os.getenv("OTHER_BOTS_PATH"))
OTHER_BOTS_URL = f"{BASE_URL}{OTHER_BOTS_PATH}"

WEB_SERVER_HOST = str(os.getenv("WEB_SERVER_HOST"))
WEB_SERVER_PORT = int(str(os.getenv("WEB_SERVER_PORT")))



# ip = os.getenv("ip")




