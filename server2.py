
import socket
import random
import time

def server():
    host = '192.168.0.188'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print("Server listening on {}:{}".format(host, port))

    while True:
        try:
            data, addr = server_socket.recvfrom(1024)

            # Simulate time delay
            delay = random.uniform(5, 10)
            time.sleep(delay)

            # Simulate dropping message with 70% probability
            if random.random() < 0.7:
                raise socket.timeout("Simulated message drop")

            print("Received data: '{}' from {}".format(data.decode(), addr))

        except socket.timeout as e:
            print("Timeout: {}".format(e))
        except socket.error as e:
            print("Socket error: {}".format(e))
        except Exception as e:
            print("Error: {}".format(e))

if __name__ == "__main__":
    server()

