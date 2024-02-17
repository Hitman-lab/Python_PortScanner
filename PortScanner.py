import pyfiglet
import socket
import time
from datetime import datetime
import sys

def scan_port(target: str):
    print("-" * 50)
    print(f"Scanning Target: {target}")
    print(f"Scan started at {str(datetime.now())}")
    print(f"-" * 50)

    try:
        startTime = time.time()
        # scanning 50 50 1000 ports - we can increase the number (1 - 65535)
        for port in range(50, 1000):
            sock_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            
            # returns an error indicator 
            result = sock_obj.connect_ex((target, port))
            if result == 0:
                print(f" Port{port} : OPEN")
            sock_obj.close()
        print("Time taken: ", time.time() - startTime)
    except socket.error:
        print("Server not responding!")
        sys.exit()


if __name__ == '__main__':
    # Add Banner 
    ascii_banner = pyfiglet.figlet_format("PORT SCANNER", font = "slant")
    print(ascii_banner)
    try:
        target = input("Enter the host to be scanned: ")
        target_IP = socket.gethostbyname(target)
        scan_port(target_IP)
    except KeyboardInterrupt:
        print("Exiting the program!")
        sys.exit()
    except socket.gaierror:
        print("Hostname could not be resolved!")
        sys.exit()
