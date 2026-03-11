
# TCP Client–Server Communication Project

## Project Description

This project demonstrates a simple **TCP client–server communication system using Python sockets**.

The server waits for a connection from a client and then receives messages sent by the client. The client connects to the server using the server’s IP address and port number and sends a message.

The goal of this project is to understand how **network communication works between two devices using TCP sockets**.

The system was tested in two ways:

1. On **localhost (two computer)**
2. Between **two devices on the same network**





| File      | Description                                      |
| --------- | ------------------------------------------------ |
| server.py | Runs the TCP server that listens for connections |
| client.py | Connects to the server and sends messages        |
| README.md | Project documentation                            |

 output:


Server started
Waiting for connection...


The server will now listen for client connections.

bash
python client.py



HOST = 10.183.168.41

Output:

Connected to server
Message sent

The server will receive and display the message.


# Test Results

## Test 1 — Localhost Two Computer)

Configuration:

Server IP: 10.183.168.41
Port: 8000

Result:

* Client successfully connected to the server
* Message was sent and received correctly

Server output:

Connection from ('20.0.30.0', 1)
Message received: Hello from client


## Test 2 — Second Device on Same WiFi

Configuration:


Server device: Laptop
Client device: Another laptop / mobile phone
Network: Same WiFi network


Result:

* Client successfully connected
* Message received by the server

 Output:

Connection from ('20.0.30.0', 1)
Message received: Hello from another device
Temperature result was sent from client to server

Through this project, the following concepts were learned:

* Basic **TCP socket programming**
* Client–server communication
* Networking between devices on the same network
* Running and testing distributed applications

# Conclusion

The TCP client–server application successfully demonstrated how two devices can communicate over a network using Python sockets. 
The system worked correctly both on **localhost** and between **two devices connected to the same WiFi network**.

