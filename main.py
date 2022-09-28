from fastapi import FastAPI, Request
import json_parser
import status_updater

app = FastAPI()


@app.post("/")
async def receiver(json_payload: dict):
    result = json_parser.parsing(json_payload)
    event_manager(result)


def event_manager(data):
    if "opened" == data["state"]:
        if "merge_request" == data["event_type"]:
            status_updater.merge_request(data)
