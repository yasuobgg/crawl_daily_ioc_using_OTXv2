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
    # Print out the ID of the first pulse in the results
    for i in range(len(results["results"])):
        pulse_id = results["results"][i]["id"]
        pulses.append(pulse_id)

    # Get all the indicators associated with a pulse
    for pulse in pulses:
        try:
            indicators = otx.get_pulse_indicators(pulse)
            for indicator in indicators:
                mongo.save_indicators(indicator)
                # print (f'{indicator["indicator"]} ({indicator["type"]}) ({indicator["created"]})')
        except indicators["indicator"].DoesNotExist:
            pass
