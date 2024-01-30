import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server's address and port
server_address = ('127.0.0.2', 12345)  # Replace 'SERVER_IP' with the actual IP address of the server machine
client_socket.connect(server_address)

# Send data to the server
message = "Hello, Server!"
client_socket.sendall(message.encode('utf-8'))
print("Sent:", message)

# Receive the response
data = client_socket.recv(1024)
print("Received:", data.decode('utf-8'))

# Close the connection
client_socket.close()

