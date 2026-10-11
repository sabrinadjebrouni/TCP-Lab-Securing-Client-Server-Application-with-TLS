from socket import *
import os
from dotenv import load_dotenv

load_dotenv()

# Read them securely
serverName = os.getenv("SERVER_IP")
serverPort = int(os.getenv("SERVER_PORT"))

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(),(serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())

clientSocket.close()