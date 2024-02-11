import socket
import time

startTime = time.time()

if __name__ == '__main__':
    target = input("Enter the host to be scanned: ")
    t_ip = socket.gethostbyname(target)
    print('Scanning started on host: ', t_ip)

    for i in range(50, 500):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn = sock.connect_ex((t_ip, i))
        if (conn == 0):
            print('Port %d: OPEN' %(i,))
        sock.close()

print("Time taken: ", time.time() - startTime)