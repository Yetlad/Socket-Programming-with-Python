import socket

def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Use "0.0.0.0" to listen on all available network interfaces
    server_ip = "0.0.0.0" 
    port = 8000

    server.bind((server_ip, port))
    server.listen(1)
    print(f"Server is listening... (Check your PC's IP via ipconfig/ifconfig)")

    client_socket, client_address = server.accept()
    print(f"Connected to: {client_address}")

    try:
        while True:
            request = client_socket.recv(1024).decode("utf-8")
            if not request or request.lower() == "close":
                break
            
            print(f"Received Data: {request}")
            client_socket.send("Data Received".encode("utf-8"))
    finally:
        client_socket.close()
        server.close()
        print("Server closed.")

run_server()