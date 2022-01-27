#!/usr/bin/python
'coded by l314ck_h4ck3l2 '

import os
import sys
import re
import builtwith
from socket import gethostbyname , gethostbyaddr


blue = '\033[34m'
green = '\033[32m'
red = '\033[31m'
yellow = '\033[33m'
error = '\033[91m'
cyan = '\033[36m'
bold    = "\033[;1m"
reset = "\033[0;0m"

ip_regex = '^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'

def banner():
    print(f"""{blue}

,-..-. .-.,---. .---.  ,---.             .--.  _______ ,-. .---.  .-. .-. 
|(||  \| || .-'/ .-. ) | .-.\  |\    /| / /\ \|__   __||(|/ .-. ) |  \| | 
(_)|   | || `-.| | |(_)| `-'/  |(\  / |/ /__\ \ )| |   (_)| | |(_)|   | | 
| || |\  || .-'| | | | |   (   (_)\/  ||  __  |(_) |   | || | | | | |\  | 
| || | |)|| |  \ `-' / | |\ \  | \  / || |  |)|  | |   | |\ `-' / | | |)| 
`-'/(  (_))\|   )---'  |_| \)\ | |\/| ||_|  (_)  `-'   `-' )---'  /(  (_) 
  (__)   (__)  (_)         (__)'-'  '-'                   (_)    (__)     


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~                        {cyan}Author : l314ck_h4ck3l2{blue}                        ~
~               {cyan}github : https://github.com/l314ck-h4ck3l2{blue}              ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

{reset}""")

def site_information(domain:str):
    site = 'http://www.' + domain or 'https://www.' + domain
    try:
        res = builtwith.builtwith(site)
        for i in res:
            print(f'{green} {i} {res[i]}{reset}')
    except:
        print(f'{red} [!] Connection Failed !{reset}')

def usage():
    print(f'{error} Usage   : python SiteInfo.py [host or ip] [port range]{reset}')
    print(f'{error} Example : python SiteInfo.py 31.13.72.174 80-85{reset}')
    print(f'{error} Example : python SiteInfo.py instagram.com 80-85{reset}')
    print(f'{error} Example : python SiteInfo.py https://www.instagram.com 80-85{reset}')
    sys.exit()

def main():
    os.system('cls' or 'clear')
    banner()
    if len(sys.argv) == 2:
        if (re.search(ip_regex, sys.argv[1])):
            addr = sys.argv[1]
            name = gethostbyaddr(addr)
        elif sys.argv[1].startswith('http://www.'):
            name = sys.argv[1][11:]
            addr = gethostbyname(name)
        elif sys.argv[1].startswith('https://www.'):
            name = sys.argv[1][12:]
            addr = gethostbyname(name)
        else:
            try:
                name = sys.argv[1]
                addr = gethostbyname(name)
            except:
                print(f'{red} [!] Host or Ip is Not True !{reset}')
                sys.exit()
        print(f'{yellow} name : {name}{reset}')
        print(f'{yellow} addr : {addr}{reset}')
        print()
        site_information(name)
    else:
        usage()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print(f'{red} [-] ^C received . shutting down server !{reset}')
        sys.exit()
