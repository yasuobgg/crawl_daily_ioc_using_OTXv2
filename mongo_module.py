from pymongo import MongoClient

from datetime import datetime

# environment variables
import os
from dotenv import load_dotenv

load_dotenv()

con_str = os.getenv("MONGO_CONNECTION_STRING")
db_name = os.getenv("MONGO_DB_NAME")
col_name_1= os.getenv("MONGO_COL_NAME_1")
col_name_2 = os.getenv("MONGO_COL_NAME_2")

# MongoDB
client = MongoClient(con_str)
db = client.get_database(db_name)

a = datetime.now()


# save indicators to mongo, ioc2
def put_iocs_to_collection(iocs):
    col = db.get_collection(f"{col_name_2}")
    for ioc in iocs:
        col.insert_one(
            {
                "timestamp": int(round(a.timestamp())),
                "type": ioc["type"],
                "data": ioc["data"],
            }
        )

# find indicators in mongo, ioc2
def find_iocs(*args):
    col = db.get_collection(f"{col_name_2}")
    return [x for x in col.find(*args, {"_id": False})]


# save pulse_id to mongo, ioc1
def find_and_put_pulses_to_collection(pulse):
    col = db.get_collection(f"{col_name_1}")
    f = col.find_one({"pulse_id": pulse})
    if f is None: # neu khong tim thay f
        col.insert_one(
            {
                "pulse_id": pulse,
            }
        )
        return pulse
    else:
        return None
