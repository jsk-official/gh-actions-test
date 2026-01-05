import os
import requests
import json

events = open(os.environ["GITHUB_EVENT_PATH"], "r")
parsed_events = json.loads(events.read())

commits_embed = {}
cnt = 1

commits_embed["fields"] = []

for i in parsed_events["commits"]:
   commits_embed["fields"].append({
      "name": "#" + str(cnt) + "by " + i["author"]["name"],
      "value": i["message"]
   })

   cnt += 1

commits_embed["title"] = str(cnt) + "new commit"

if cnt > 1:
   commits_embed["title"] += "s"

commits_embed["description"] = "Branch: Unknown"

print(commits_embed)

response = requests.post(os.environ["COMMITS_CHANNEL_WEBHOOK"], {
   "username": "Armored Patrol Remastered Changelogs",
   "avatar_url": "https://cdn.discordapp.com/icons/1021084114343952484/db5194b83958a75d14cf2e84a715cddb.webp?size=256&quality=lossless",
   "embeds": [commits_embed],
})

print(response.text)
