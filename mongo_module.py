from pymongo import MongoClient

from datetime import datetime

# environment variables
import os
from dotenv import load_dotenv

load_dotenv()

server = os.getenv("MONGO_SERVER")
port = int(os.getenv("MONGO_PORT"))
db_name = os.getenv("MONGO_DB_NAME")
col_name = os.getenv("MONGO_COL_NAME")

# MongoDB
client = MongoClient(server, port)
db = client.get_database(db_name)

a = datetime.now()


# save indicators to mongo
def put_iocs_to_collection(iocs):

    col = db.get_collection(f"{col_name}")

    col.insert_one(
        {
            "timestamp": int(round(a.timestamp())),
            "type": iocs["type"],
            "data": iocs["data"],
        }
    )

# find indicators in mongo
def find_indicators(*args):
    col = db.get_collection(f"{col_name}")
    return [x for x in col.find(*args, {"_id": False})]
