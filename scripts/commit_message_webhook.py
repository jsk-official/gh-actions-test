import os
import requests
import json

events = open(os.environ["GITHUB_EVENT_PATH"], "r")
parsed_events = json.loads(events.read())

message_content = ""

for i in parsed_events["commits"]:
   message_content += i['message'] + ' - ' + i['author']['name'] + '\n'

requests.post(os.environ["COMMITS_CHANNEL_WEBHOOK"], {
   "content": message_content
})
