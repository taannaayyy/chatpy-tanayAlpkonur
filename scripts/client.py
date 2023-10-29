import threading
import socket

name = input("Please enter your name >>> ")

# creates the client object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connects the client to the localhost and port
client.connect(('localhost', 8765))


# function to handle receiving messages from the server
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            # if 'name?' message is equal to the received message send the name to the server
            if message == 'name?':
                client.send(name.encode('utf-8'))

            # prints the messages received from the server
            else:
                print(message)
        # handles any errors and closes the connection with that client, breaks out of the loop
        except:
            print("ERROR!")
            client.close()
            break


# function to read messages from the clients
def client_send():
    while True:
        message = f'{name}: {input("")}'
        client.send(message.encode('utf-8'))


# creates and starts the threads
receive_thread = threading.Thread(target=receive)
receive_thread.start()
send_thread = threading.Thread(target=client_send())
send_thread.start()
