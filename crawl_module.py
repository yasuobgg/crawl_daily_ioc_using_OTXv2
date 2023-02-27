from OTXv2 import OTXv2

import os
from dotenv import load_dotenv

import mongo_module as mongo

load_dotenv()
otx_api_key = os.getenv("OTX_API_KEY")
otx = OTXv2(api_key=otx_api_key)

# Search for pulses containing the term "malware"
results = otx.search_pulses("malware")


def find_all_indicators_and_save_to_mongo():
    pulses = []
    iocs = []
    # Get all pulses_id of results
    for i in range(len(results["results"])):
        pulse_id = results["results"][i]["id"]
        pulses.append(pulse_id)

    # Get all the indicators associated with a pulse
    for pulse in pulses:
        indicators = otx.get_pulse_indicators(pulse)
        for indicator in indicators:
            iocs.append(indicator)

    # Group all iocs by type, iocs in list data[], like this:
    #     {
    #     "timestamp": 012345678,
    #     "type": "asdf",
    #     "data": [],
    #      }
    grouped_dict = {}
    for item in iocs:
        type = item["type"]
        if type in grouped_dict:
            grouped_dict[type].append(item["indicator"])
        else:
            grouped_dict[type] = [item["indicator"]]

    grouped_list = []
    for type, items in grouped_dict.items():
        grouped_list.append({"type": type.replace("FileHash-", ""), "data": items})

    # For loop to save all items to mongodb
    for item in grouped_list:
        mongo.save_indicators(item)
