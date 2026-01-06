import os
import requests
import json

events = open(os.environ["GITHUB_EVENT_PATH"], "r")
parsed_events = json.loads(events.read())

commits_embed = {
   "title": "Changelog",
   "footer": {
      "text": "Branch: main",
   },
   "color": 0x206694,
}

cnt = 0
desc = ""

for i in parsed_events["commits"]:
   if cnt == 24:
      desc += "Truncated to the last 24 commits."
      
      break

   desc += i["message"] + " - " + i["author"]["name"] + "\n"
   cnt += 1

print(parsed_events)
commits_embed["title"] = "[" + parsed_events["name"] + parsed_events["ref"].replace("refs/heads/", "") + "] " + str(cnt) + " new commit"

if cnt > 1:
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
else:
   exit(1) #didn't find any commits
