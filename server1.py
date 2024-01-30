import socket

def Main():
   
    host = '192.168.0.181' #Server ip
    port = 4000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    

    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    s.bind((host, port))

    print("Server Started")
    while True:
        # data, addr = s.recvfrom(1024)
        # data = data.decode('utf-8')
        # print("Message from: " + str(addr))
        # print("From connected user: " + data)
        # data = data.upper()
        data = input("->")
        print("Sending: " + data)
        s.sendto(data.encode('utf-8'), ('192.168.0.255', 5005))
    c.close()

if __name__=='__main__':
    Main()