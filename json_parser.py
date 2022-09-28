import json
import re


def parsing(data):
    issue = data["object_attributes"]["description"]
    pattern = "AM-[0-9]+"
    result = re.findall(pattern, issue)

    req_data = {
        "title": data["object_attributes"]["title"],
        "issue_id": result,
        "event_type": data["object_kind"],
        "state": data["object_attributes"]["state"],
    }
    return req_data

    # for k,v in data.items():
    #     if type(v) is dict:
    #         yield from parsing(v)
    #     if "labels" == k:
    #         yield True
