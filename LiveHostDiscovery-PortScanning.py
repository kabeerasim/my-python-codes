import argparse
import socket
import datetime
from colorama import Fore, Style
import re
from easyprocess import subprocess
import time


portlist = [1,5,7,9,11,13,17,18,19,20,21,22,23,25,37,39,42,43,49,50,53,
67,68,69,70,71,79,80,81,82,88,101,102,105,107,109,110,111,113,115,117,119,
137,139,143,161,162,177,179,201,209,210,213,220,369,370,389,427,444,443,445,464,
500,512,512,513,513,514,514,515,517,518,520,520,521,525,530,531,532,533,540,
543,544,546,547,548,554,556,563,587,631,631,636,674,694,749,750,873,992,993,995
]

portlist = [1, 2, 4, 21, 22, 23, 25, 135] # Remove this line if you want to scan all the above ports.

def main(args, ipadress):

    if args.sL:

        print(f"[ Sending ICMP Packet to {Fore.RED}{ipadress}{Style.RESET_ALL} for Live Host Discovery ]")
        ping = subprocess.call(f'ping -n 1 {args.ip}') # Simply pinging the device

    elif args.sP:

        print(f"[ Scanning {Fore.RED}{ipadress}{Style.RESET_ALL} for open ports ]")
        now = str(datetime.datetime.now()).split(" ")[1].split(".")[0]
        print(f"Started at: {now}")
        openports = []
        junk = []

        for port in portlist:
            try: 
                sock = socket.socket()
                sock.connect((ipadress, port)) # Connecting with the device on the specific port
                sock.settimeout(0.5)
                openports.append(port)

            except:
                junk.append("1") # Just for Exception Handling

        if len(openports) >= 1: # Printing out specific results if there is any open port founded or not.

            print(f"{Fore.BLUE}Open Ports Founded:{Style.RESET_ALL}")
            for i in openports:
                print(f"{Fore.RED}{i}{Style.RESET_ALL}")
            now = str(datetime.datetime.now()).split(" ")[1].split(".")[0]
            print(f"Ended at: {now}")

        else:
            print(f"{Fore.BLUE}No Open Ports Founded{Style.RESET_ALL}")
            now = str(datetime.datetime.now()).split(" ")[1].split(".")[0]
            print(f"Ended at: {now}")

    elif args.A:

        message = ""
        megalist = []
        open_ports = []
        junk = []
        check = ipadress.split(".")[3] # Spliting the IP by . and jumping to the last octet
        matched = re.findall("-", ipadress) # Finding any '-' in the last octet so that we can know if the user wants Live Host Discovery and Port Scanning on a range of ip or a single one.

        is_match = bool(matched) 

        if len(check) <= 3 and is_match == False: 
            print(f"[ {Fore.BLUE}Pinging{Style.RESET_ALL} {Fore.RED}{ipadress}{Style.RESET_ALL} for Live Host Discovery ]")
            ping = subprocess.call(f'ping -n 1 {ipadress}')

            print(f"[ {Fore.BLUE}Scanning{Style.RESET_ALL} {Fore.RED}{ipadress}{Style.RESET_ALL} for Open Ports]")
            for port in portlist:

                try:
                    sock = socket.socket()
                    sock.connect((ipadress, port))
                    sock.settimeout(0.5)
                    open_ports.append(port)

                except:
                    junk.append('1')

            if len(open_ports) >= 1:

                print(f"{Fore.BLUE}Open Ports Founded:{Style.RESET_ALL}")
                for i in open_ports:
                    print(f"{Fore.RED}{i}{Style.RESET_ALL}")
                now = str(datetime.datetime.now()).split(" ")[1].split(".")[0]
                print(f"Ended at: {now}")
            else:
                print(f"{Fore.BLUE}No Open Ports Founded{Style.RESET_ALL}")
                now = str(datetime.datetime.now()).split(" ")[1].split(".")[0]
                print(f"Ended at: {now}")

        elif len(check) >= 3 and is_match == True:
            print(f"[ {Fore.BLUE}Scanning{Style.RESET_ALL} {Fore.RED}{ipadress}{Style.RESET_ALL} for Open Ports]")

            try: 
                first = check.split("-")[0]
                first = int(first)
                second = check.split("-")[1]
                second = int(second)
                for ip in range(first, second):
                    new = f'{ipadress.split(".")[0]}.{ipadress.split(".")[1]}.{ipadress.split(".")[2]}.{ip}'
                    for port in portlist:
                        try:                            
                            sock = socket.socket()
                            sock.settimeout(0.5)
                            sock.connect((new, port))
                            open_ports.append(port)
                        except:
                            junk.append('1')
                    print( f'{Fore.BLUE}Scanned{Style.RESET_ALL} {Fore.RED}{new}{Style.RESET_ALL}: {Fore.BLUE}Founded:{Style.RESET_ALL} {Fore.RED}{open_ports}{Style.RESET_ALL}\n')
                    open_ports = [' ']
                print(message)
            except Exception as e:
                print(e)
        else:
            pass
if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--sL', type=str, help="For Single Live Host Discovery, --sL y. ")

    parser.add_argument(
        '--sP', type=str, help="For Single Host Port Scanning, --sP y. ")

    parser.add_argument(
        '--A', type=str, help="For All Live Hosts and their Port Scanning, --aLP y.")

    parser.add_argument(
        '--ip', type=str, default='192.168.10.1', help="Enter The Target IP Adress here")

    args = parser.parse_args()  # Parsing all the arguments created above
    ipadress = str(args.ip)
    main(args, ipadress)
