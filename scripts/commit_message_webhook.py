import os
import requests

print(os.environ["commitmsg"])
print(os.environ["author"])

requests.post(os.environ["COMMITS_CHANNEL_WEBHOOK"], {
   "content": os.environ["commitmsg"] + " - " + os.environ["author"]
})
