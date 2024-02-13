import socket

def client():
    # Get the host name (as both server and client code are running on your PC)
    host = socket.gethostname()
    # Define the server's port number to interact with
    port = 21042

    # Create a socket object
    client_socket = socket.socket()

    # Set the socket to non-blocking
    client_socket.setblocking(1)

    # Connect to the server by specifying the hostname and port number
    try:
        client_socket.connect((host, port))
    except BlockingIOError:
        pass  # Connection in progress

    # Prompt the user for input
    message = input("Enter your message (Type 'bye' to exit): ")
    while message.lower().strip() != "bye":
        try:
            # Send the message to the server
            client_socket.send(message.encode())
            # Receive a response from the server
            data = client_socket.recv(1024).decode()
            # Display the received message from the server
            print("Received from server: " + data)
        except BlockingIOError:
            pass  # No data received yet

        # Prompt for the next message
        message = input("Enter your message (Type 'bye' to exit): ")

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    client()
