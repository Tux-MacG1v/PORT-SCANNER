
import os.path
import os
import sys
import time
import socket
from concurrent.futures import ThreadPoolExecutor
from importlib import reload
from colorama import init, Fore, Style

init(autoreset=True)

reload(sys)
r = Fore.RED + Style.BRIGHT
g = Fore.GREEN + Style.BRIGHT
c = Fore.CYAN + Style.BRIGHT
y = Fore.YELLOW + Style.BRIGHT
o = Fore.RESET + Style.RESET_ALL

good = []
bad = []
failed = []

banner = """
                   {}[!] {}NOSLEEP {} - {}PORT SCANNER{}
                        {}CODED BY TUX-MACG1V{}
                   {}https://github.com/Tux-MacG1v{}
                    
""".format(r, g, y, g, o, r, o, y, o, r, o, g, o)



def ip(i):
    global portt, timeouuut
    try:
        sites = i.replace('\n', '').replace('\r', '')
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(float(timeouuut))
        result = sock.connect_ex((sites, int(portt)))
        if str(result) != '0':
            bad.append(i)
            print("{}[-] IP:{}{} {}PORT:{}{} {}[CLOSE PORT]{}".format(r, c, sites, y, c, portt, r, o))
            open("Bad.txt", "a").write(sites + "\n")
        elif str(result) == '0':
            good.append(i)
            print("{}[+] IP:{}{} {}PORT:{}{} {}[OPEN PORT]{}".format(g, c, sites, y, c, portt, g, o))
            open("Live.txt", "a").write(sites + "\n")
        else:
            bad.append(i)
            print("{}[-]IP:{}{} {}PORT:{}{} {}[BAD IP]{}".format(r, c, sites, y, c, portt, r, o))
    except:
        print("{}[!] [INPUT PROBLEM]".format(r))
        pass
        failed.append(i)
        time.sleep(5)
        sys.exit()



def main():
    try:
        global portt, timeouuut
        os.system('cls' if os.name == 'nt' else 'clear')
        print(banner)
        lists = input('\n{}[+] {}IP List{} > {}'.format(c, g, o, g).strip())
        power = int(input('{}[+] {}Thread{} > {}'.format(c, g, o, r, r)))
        portt = int(input('{}[+] {}PORT{} > {}'.format(c, g, o, r, r)))
        timeouuut = input('{}[+] {}TIMEOUT{} > {}'.format(c, g, o, r, r))
        print('')

        def runner():
            threads = []
            domain = lists.replace('"', '')
            process = open(domain, 'r').read().splitlines()
            with ThreadPoolExecutor(max_workers=power) as thread:
                [threads.append(thread.submit(ip, i)) for i in process]

        runner()
        print("\n\n{}[+] TOTAL GOODS {}: {}[{}{}{}]{}".format(g, o, g, o, str(len(good)), g, o))
        print("{}[-] TOTAL BADS {}: {}[{}{}{}]{}".format(c, o, c, o, str(len(bad)), r, o))
        print("{}[!] TOTAL FAILED {}: {}[{}{}{}]{}".format(r, o, r, o, str(len(failed)), r, o))
        time.sleep(100)
    except Exception as e:
        print('{}[!] {}Incorrect'.format(c, r))
        time.sleep(0.5)


if __name__ == '__main__':
    main()
