#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# local lib
import crawl_module as crawl
import mongo_module as mongo

# web app lib
from sanic import Sanic
from sanic.response import json as sjson
from sanic_cors import CORS

# basic lib
import json

# Scheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

app = Sanic(__name__)
app.config["DEBUG"] = True
CORS(app)


# find daily indicator and save to mongodb
def daily_crawl():
    # iocs = crawl_module.find_all_indicators_and_save_to_mongo()
    mongo.put_iocs_to_collection(crawl.find_all_indicators_and_save_to_mongo())


@app.route("/api/v1", methods=["POST"])
def get_data(request):
    param = json.loads(request.body)  # get the body of the request sent by postman
    print(param)
    ftype = param["type"]  

    if ftype == "MD5" or ftype == "IPv4" or ftype == "domain": # type of data to query
        res = mongo.find_iocs(param)  # find in mongodb
    else:
        res = {"Type error": "Unavailable"}

    return sjson(res, headers={'X-Served-By': 'CMC SOC'}) # return response + headers


# schedule everyday at 7 AM
scheduler = BackgroundScheduler()
trigger = CronTrigger(year="*", month="*", day="*", hour="7", minute="0", second="0")
scheduler.add_job(
    daily_crawl,
    trigger=trigger,
    name="daily pull",
)
scheduler.start()

if __name__ == "__main__":
    # daily_crawl()
    app.run(host="0.0.0.0", port=8000, debug=False, auto_reload=True)
