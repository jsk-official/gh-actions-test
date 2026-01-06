import os
import requests
import json

events = open(os.environ["GITHUB_EVENT_PATH"], "r")
parsed_events = json.loads(events.read())

commits_embed = {
   "title": "Changelog",
   "color": 0x206694,
   "url": parsed_events["sender"]["html_url"],
}

commits_embed["author"] = {
   "name": parsed_events["sender"]["login"],
   "icon_url": parsed_events["sender"]["avatar_url"],
   "url": parsed_events["sender"]["html_url"],
}

cnt = 0
desc = ""
   
for i in parsed_events["commits"]:
   if cnt == 25:      
      break
   
   desc += "`{}` {} - {} \n".format(i["id"][:7], i["message"].split("\n")[0], i["author"]["username"])
   cnt += 1

commits_embed["title"] = "[{}:{}] {} {}".format(parsed_events["repository"]["name"], parsed_events["ref"].replace("refs/heads/", ""), (cnt >= 25 and "25+" or str(cnt)), (cnt >= 1 and "new commit" or "new commits"))

parsed_events["commits"].reverse() # we do this so that in Discord, the commits show the latest first and the oldest last
# instead of oldest first and latest last

if cnt >= 1:
   commits_embed["description"] = desc
   
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
   print("No commits found")
   
   exit(1)
