import os
import requests
import json

events = open(os.environ["GITHUB_EVENT_PATH"], "r")
parsed_events = json.loads(events.read())

commits_embed = {
   "title": "Changelog",
   "description": "Branch: unknown",
   "fields": [],
}

cnt = 1

for i in parsed_events["commits"]:
   print(i)
   
   commits_embed["fields"].append({
      "name": "#" + str(cnt) + " by " + i["author"]["name"],
      "value": i["message"]
   })

   cnt += 1

commits_embed["title"] = str(cnt) + " new commit"

if cnt > 1:
   commits_embed["title"] += "s"

print(json.dumps(commits_embed, indent=4))

response = requests.post(os.environ["COMMITS_CHANNEL_WEBHOOK"], json={
   "username": "Armored Patrol Remastered Changelogs",
   "avatar_url": "https://cdn.discordapp.com/icons/1021084114343952484/db5194b83958a75d14cf2e84a715cddb.webp?size=256&quality=lossless",
   "content": "Detected a new change to the Armored Patrol Remastered development repository.",
   "embeds": [commits_embed],
})

print(response.text)

if response.status_code != 204:
   exit(1)
