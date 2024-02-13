import socket

def server():
    # Get the hostname of the server
    host = socket.gethostname()

    # Specify the port to listen on
    port = 21042

    # Create a socket object
    s = socket.socket()

    # Set the socket to non-blocking
    s.setblocking(1)

    # Bind the socket to the host and port
    s.bind((host, port))
    
    # Listen for incoming connections, allowing up to 2 clients in the queue
    s.listen(2)

    # Initialize the client socket to None
    c = None

    while True:
        try:
            # Accept an incoming connection
            c, address = s.accept()
            print(f"Connected to: {address}")
        except BlockingIOError:
            pass  # No incoming connection yet

        if c:
            try:
                # Receive data from the client (up to 1024 bytes) and decode it
                data = c.recv(1024).decode()
                # If no data is received, break the loop
                if not data:
                    break
                print(f"Received from client: {data}")

                # Get user input and send it to the client after encoding
                response = input("Enter response to send to client: ")
                c.send(response.encode())
            except BlockingIOError:
                pass  # No data received yet

    # Close the client connection
    if c:
        c.close()

if __name__ == "__main__":
    # Start the server
    server()