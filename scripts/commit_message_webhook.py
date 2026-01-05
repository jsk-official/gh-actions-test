import os
import requests
import json

events = open(os.environ["GITHUB_EVENT_PATH"], "r")
parsed_events = json.loads(events.read())

for i in parsed_events["commits"]:
   print(i)

print(os.environ["author"])

requests.post(os.environ["COMMITS_CHANNEL_WEBHOOK"], {
   "content": os.environ["author"] + " - " + os.environ["author"]
})
