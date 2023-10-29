import threading
import socket

host = 'localhost'
port = 8765

# create a server object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the server to the host and the port
server.bind((host, port))
# activate the listening mode for any incoming connections to the server
server.listen()

# lists to store active clients and their name
clients = []
names = []


# function to send a message to all the connected clients.
# it iterates through the list of clients and sends the message to each client
def broadcast(message):
    for client in clients:
        client.send(message)


# function to handle incoming messages from clients and sends them to chatroom
def handle(client):
    while True:
        try:
            # maximum amount of bytes that the server can receive from client
            message = client.recv(1024)
            # if a message received successfully from the client broadcast
            # function invoked to send the message to the chatroom
            broadcast(message)
        except:
            # if a client disconnects or an error occurs, that client is removed
            # from the chatroom and closed their connection
            index = clients.index(client)
            clients.remove(client)
            client.close()
            name = names[index]
            print(f'{name} left the chat')
            broadcast(f'{name} left the chat'.encode('utf-8'))
            names.remove(name)
            break


# main function to receive clients connections.
def receive():
    while True:
        print('server is running successfully and listening')
        # lets the server be ready to accepts any incoming connections
        client, address = server.accept()
        print(f'connection is established with {str(address)}')
        # request the clients' name and store it.
        client.send('name?'.encode('utf-8'))
        name = client.recv(1024).decode('utf-8')
        names.append(name)
        clients.append(client)
        # displays a message in server saying that the name of the client is 'client's name'
        print(f'name of the newcomer is {name}')
        # sends a message to all connected clients that new user connected to the chat
        broadcast(f'{name} has connected to the chatroom \n'.encode('utf-8'))
        client.send(f'you are now connected'.encode('utf-8'))
        # creates the thread object and starts it
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


# starts the server
if __name__ == "__main__":
    receive()
