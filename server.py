import socket
import threading
import pyfiglet

B='\033[1;34m'
C='\033[1;37m'
CY='\033[1;36m'
Y='\033[1;33m'
G='\033[1;32m'
RT='\033[;0m'
R = "\033[1;31m"

figlet = pyfiglet.figlet_format("Server",font="banner3-D")
print(Y+figlet,C)
print(f'{R}                                     [Version: 0.1]{C}')
print(f"[{Y}i{C}] Recomendamos que Use portas Acima de 2000")
HOST = input("[ Host ]: ")
PORT = int(input("[ Port ]: "))

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()
print(f'O servidor está ativo  {HOST}:{PORT}')

clients = []
usernames = []

def globalMessage(message):
    for client in clients:
        client.send(messageasernames[clientLeaved])
        print(f'{clientLeavedUsername} saiu do chat...')
        globalMessage(f'{clientLeavedUsername} deixou...'.encode('ascii'))
        usernames.remove(clientLeavedUsername)


def initialConnection():
    while True:
        try:
            client, address = server.accept()
            print(f"Conexão nova: {str(address)}")
            clients.append(client)
            client.send('getUser'.encode('ascii'))
            username = client.recv(2048).decode('ascii')
            usernames.append(username)
            globalMessage(f'{username} entrou no chast!!'.encode('ascii'))
            user_thread = threading.Thread(target=handleMessages,args=(client,))
            user_thread.start()
        except:
            pass

initialConnection()
