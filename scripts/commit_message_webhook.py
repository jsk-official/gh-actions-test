import os
import requests

print(os.environ["commitmsg"])
print(os.environ["author"])

print(os.environ["GITHUB_EVENT_PATH"])

requests.post(os.environ["COMMITS_CHANNEL_WEBHOOK"], {
   "content": os.environ["commitmsg"] + " - " + os.environ["author"]
})
