Python Chatting Application Using Socket and Thread Libraries


1)	Brief introduction as the purpose of the software

The Python Chat Room is a simple chat application built using sockets and threads. 
It allows users to connect to local host “127.0.0.1”, port “8765” and communicate in real-time through a text.
	
2)	Manual describing how it should be used 

Prerequisites
•	Python 3.x installed
Getting Started
1.	Clone this repository to your local machine.
2.	Open a terminal/command prompt and navigate to the project directory.
3.	Start the server by running python server.py.
4.	Connect to the server using a client by running python client.py.
5.	Follow the on-screen prompts to enter your username and start chatting.

3)	Possible safety concerns it might have

Limited Security: This application does not implement advanced security features.

Error handling: If a client disconnects or an error occurs, that client is removed from the chatroom and their connection closes. 

Data Privacy: Since the messages are transmitted in plain text using ‘utf-8’, there's a risk of data tampering.


