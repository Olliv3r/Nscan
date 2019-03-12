#!/usr/bin/env python3
# Autor: olive
# Nome: Nmap

import nmap
import os
import subprocess
import time
import sys

args1, args2 = sys.argv[1], sys.argv[2]

n = nmap.PortScanner()

class nmap:
    def __init__(scanner, target, portas):
        scanner.target = args1
        scanner.portas = args2
        
        subprocess.run('clear')
        os.system("sh banner.sh")
        time.sleep(1)
        print ("\n\033[01;92mScaneando... > \033[01;93m{} \033[01;92mPortas > \033[01;93m{}\033[0m".format(args1, args2))
        n.scan(scanner.target, scanner.portas)
        print("\033[01;96mResultados\033[0m\n") 
        for host in n.all_hosts():
            print("\033[01;93mIP: \033[01;91m{}, \033[01;93mSite: \033[01;91m{}\033[0m".format(host, n[host].hostname()))
            for proto in n[host].all_protocols():
                print("\033[01;93mProtocolo: \033[01;91m{}\033[0m".format(proto))
                print("\033[01;93mState: \033[01;91m{}\033[0m".format(n[host].state()))
                lport = n[host][proto].keys()
                lport = list(lport)
                lport.sort()

                for porta in lport:
                    print("\033[01;93mPorta: \033[01;91m{}, \033[01;93mEstado: \033[01;91m{}\033[0m".format(porta, n[host][proto][porta]['state']))
                    print ("")


    def imprime(scanner):
        print("\033[01;94mScanner completo\033[0m")

resultados = nmap(args1, args2)
resultados.imprime()
