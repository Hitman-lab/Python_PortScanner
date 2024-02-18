import socket 
import time, sys, pyfiglet
import threading
from queue import Queue
from datetime import datetime

PRINT_LOCK = threading.Lock()  
q = Queue() 
ascii_banner = pyfiglet.figlet_format("PORT SCANNER", font = "slant")
print(ascii_banner)

# user input 
try:
    target = input("Enter the host to be scanned: ")
    t_ip = socket.gethostbyname(target)
except KeyboardInterrupt:
    print("Exiting the program!")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved!")
    sys.exit()

print(f"-" * 50)
print(f"Scanning Target: {t_ip}")
print(f"Scan started at {str(datetime.now())}")
print(f"-" * 50)

def port_scan(port): # port scan method 
    s_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.25)
    try:
        conn = s_obj.connect((t_ip, port))
        with PRINT_LOCK: # thread synchronization 
            print(f"Port: {port} OPEN")
        s_obj.close() 
    except: 
        pass

def threader():
    while True:
        worker = q.get() # consuming the port number
        port_scan(worker) # here worker is the port number
        q.task_done()

startTime = time.time()
for x in range(100):
    t = threading.Thread(target = threader)
    t.daemon = True
    t.start()

for worker in range(1, 500): # fixed range of port numbers
    q.put(worker)

q.join()
print(f"-" * 50)
print('Time Taken: %0.2f ' %(time.time() - startTime))