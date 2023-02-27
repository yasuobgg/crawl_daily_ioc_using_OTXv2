import crawl_module
import mongo_module

from flask import Flask, jsonify, request

from flask_cors import CORS

# Scheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

app = Flask(__name__)
CORS(app)


# find daily indicator and save to mongodb
def daily_crawl():
    crawl_module.find_all_indicators_and_save_to_mongo()


@app.route("/app", methods=["GET"])
def get_data():
    param = request.get_json()
    print(param)
    res = mongo_module.find_indicators(param)
    return jsonify(
        res,
    )


@app.route("/deleteall", methods=["DELETE"])
def delete_all():
    mongo_module.delete_all_data()
    return (jsonify(""), 202)


# daily_crawl()

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
    app.run(port=5678, debug=True)
