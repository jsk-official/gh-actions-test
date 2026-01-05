import os
import requests

print(os.environ["author"])

print(os.environ["GITHUB_EVENT_PATH"])

requests.post(os.environ["COMMITS_CHANNEL_WEBHOOK"], {
   "content": os.environ["author"] + " - " + os.environ["author"]
})
