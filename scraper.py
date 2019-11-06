import requests
import sys

def write_to_file(userId, content):
    with open(str(userId), "w") as write_to:
        write_to.write(str(content))
        print("done!")

def scrape_user(userId):
    headers = {
	"Host": "friends.roblox.com",
	"User-Agent": "",
	"Accept": "",
        "Accept-Language": "",
	"Accept-Encoding": "",
	"Cookie": "",
    }

    response = requests.get("https://friends.roblox.com/v1/users/" + str(userId) + "/friends/online", headers=headers)
	
    #{
    #  "userPresence": {
    #    "UserPresenceType": "{website,game,studio,etc}",
    #    "lastLocation": "{lastlocationname}",
    #    "placeId": {placeid},
    #    "rootPlaceId": {rootplaceid},
    #    "gameInstanceId": "{gameinstance}",
    #    "universeId": {universeid},
    #    "lastOnline": "{timestamp}"
    #  },
    #  "id": {userid},
    #  "name": "{username}"
    #},

    if response.status_code == 200:
        write_to_file(userId, response.content)
    else:
        print("user banned!")

for i in range(100): # userId range (E.g. 30 million).
    print("userId: " + str(i))
    scrape_user(i)
