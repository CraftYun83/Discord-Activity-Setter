import psutil, json, time, requests, atexit

with open("activities.json", "r") as actfile:
    activities = json.loads(actfile.read())
current_app = ""

def setStatusText(text):

    url = "https://discord.com/api/v9/users/@me/settings"

    payload = json.dumps({
        "custom_status": {
            "text": text
        }
    })
    headers = {
        'authority': 'discord.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': '<TOKEN>',
        'content-type': 'application/json',
        'origin': 'https://discord.com',
        'referer': 'https://discord.com/channels/@me/999247778351939604',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-discord-locale': 'en-US',
    }

    requests.request("PATCH", url, headers=headers, data=payload)

def changeOnOrOff(status):

    url = "https://discord.com/api/v9/users/@me/settings"

    payload = json.dumps({
        "status": status
    })
    headers = {
        'authority': 'discord.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': '<TOKEN>',
        'content-type': 'application/json',
        'origin': 'https://discord.com',
        'referer': 'https://discord.com/channels/@me/999247778351939604',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-discord-locale': 'en-US',    }

    requests.request("PATCH", url, headers=headers, data=payload)


def changeStatus():
    if current_app == "":
        text = ""
        status = "invisible"
    else:
        text = activities[current_app]["status_message"]
        status = "online"

    changeOnOrOff(status)
    setStatusText(text)

def exit_handler():
    changeOnOrOff("invisible")
    setStatusText("")

atexit.register(exit_handler)

while True:
    queued_app = ""
    for app in activities:
        if activities[app]["app"] in (i.name() for i in psutil.process_iter()):
            if queued_app == "":
                queued_app = app
            else:
                if activities[app]["priority"] > activities[queued_app]["priority"]:
                    queued_app = app
    
    if queued_app != current_app:
        current_app = queued_app
        changeStatus()
    
    time.sleep(2)
