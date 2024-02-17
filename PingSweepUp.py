import os
import sys
import pyfiglet
import platform
import ipaddress
import time

def sweep_config(ip):
    net1 = ip.split('.')
    net2 = net1[0] + '.' + net1[1] + '.' + net1[2] + '.'
    try:
        num1 = int(input('Enter Starting number: '))
        num2 = int(input('Enter Ending number: '))
        num2 += 1
    except:
        print("Invalid String! Enter in number format.")
        sys.exit()

    # checking which flatform pgm is running
    ch_pt = platform.system()
    if ch_pt == 'Windows':
        ping1 = 'ping -n 1 '
    elif ch_pt == 'Linux': 
        ping1 = 'ping -c 1 '
    else:
        ping1 = 'ping -n 1 '
    
    startTime = time.time()
    print("-" * 100)
    print(f"Scanning in progress......")
    for n in range(num1, num2):
        addr = net2 + str(n) # ip address 
        # print(addr)
        command = ping1 + addr
        response = os.popen(command) # return a file object

        for line in response.readlines():
            line = line.rstrip() # removes new line char from the end
            # print(line)
            if (line.count('TTL') or line.count('ttl')):
                print(f'{addr} --> Live!')

    totalTimeTaken = time.time() - startTime
    print('Scanning completed in: %.2f Sec' %totalTimeTaken)
    return


if __name__ == "__main__":
    # add banner
    ascii_banner = pyfiglet.figlet_format("PingSweep Scanner", font="slant")
    print(ascii_banner)
    try:
        user_input = input('Enter an IP address:').strip()
        ip_addr = ipaddress.IPv4Address(user_input)
        sweep_config(str(ip_addr))
    except ValueError as e:
        print(f"Enter a valid IPv4 Address {e}")
        sys.exit()
    except KeyboardInterrupt:
        print("Uh oh! Try again !!")
        sys.exit()