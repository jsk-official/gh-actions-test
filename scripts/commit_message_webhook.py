import os
import requests
import json

events = open(os.environ["GITHUB_EVENT_PATH"], "r")
parsed_events = json.loads(events.read())

commits_embed = {
   "title": "Changelog",
   "fields": [],
   "footer": {
      "text": "Branch: main",
   },
   "color": 0x206694,
}

cnt = 0

for i in parsed_events["commits"]:
   if cnt == 25:
      break
   
   cnt += 1

   commits_embed["fields"].append({
      "name": "#" + str(cnt) + " by " + i["author"]["name"],
      "value": i["message"]
   })

commits_embed["title"] = str(cnt) + " new commit"
commits_embed["footer"]["text"] = "Branch: " + parsed_events["ref"].replace("ref/heads/", "")

print(parsed_events["ref"].replace("ref/heads/", ""))

if cnt > 1 or cnt == 0:
   commits_embed["title"] += "s"

response = requests.post(os.environ["COMMITS_CHANNEL_WEBHOOK"], json={
   "username": "Armored Patrol Remastered Changelogs",
   "avatar_url": "https://cdn.discordapp.com/icons/1021084114343952484/db5194b83958a75d14cf2e84a715cddb.webp?size=256&quality=lossless",
   "content": "Detected a new change to the Armored Patrol Remastered development repository.",
   "embeds": [commits_embed],
})

if response.status_code != 204:
   print(response.text)
   
   exit(1)
