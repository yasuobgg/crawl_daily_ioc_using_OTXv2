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
    # All types of searching for IOCs
    types = [
        "IOCs",
        "malware",
        "IP addresses",
        "Domains",
        "URLs",
        "File hashes",
        "Email addresses",
    ]
    iocs = []
    # Get all iocs of pulses found
    for mane in types:
        results = otx.search_pulses(mane)
        for result in results["results"]:
            indicators = otx.get_pulse_indicators(result["id"])
            for indicator in indicators:
                iocs.append(indicator)

    # Group all iocs by type, iocs in a group_list, like this:
    # [
    #   {
    #     "timestamp": 012345678,"type": "asdf","data": [],
    #   },
    #   {......},
    #   {......},
    # ]

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
