import os
import requests
import json

events = open(os.environ["GITHUB_EVENT_PATH"], "r")
parsed_events = json.loads(events.read())

commits = {}
cnt = 1

commits["fields"] = []


for i in parsed_events["commits"]:
   commits["fields"].append({
      "name": "#" + cnt + "by " + i["author"]["name"],
      "value": i["message"]
   })

   cnt += 1

commits["footer"] = {
   "text": "Branch: unknown"
}

print(commits)

requests.post(os.environ["COMMITS_CHANNEL_WEBHOOK"], {
   "username": "Armored Patrol Remastered Changelogs",
   "avatar_url": "https://cdn.discordapp.com/icons/1021084114343952484/db5194b83958a75d14cf2e84a715cddb.webp?size=256&quality=lossless",
   "embeds": commits,
})
