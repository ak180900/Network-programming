import socket
import time

def main():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    # Enable broadcasting mode
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    # Bind the socket to a specific port
    sock.bind(('0.0.0.0', 5005))

    while True:
        # Send a message to all devices on the network
        sock.sendto(b'test', ('255.255.255.255', 5005))
        time.sleep(1)

if __name__ == '__main__':
    main()
