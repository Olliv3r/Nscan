#!/bin/env python3
# Name: Nscan
# Describe: Escaner de portas de serviços remotos
# Lisense: MIT Lisense
# Author: Olive <https://tecnospeed.000webhostapp.com/>
# Version: 2.1

# Necessary modules:
from os import system
import argparse
import nmap
import time

# Check necessary dependencies:
def check():
    requires = ['tput', 'figlet']
    _bin = '/data/data/com.termux/files/usr/bin'
    _bin = list(_bin)
    _bin.sort()
    for packageRequired in requires:
        text = "Requires Package => {}".format(packageRequired)
        if(packageRequired not in _bin):
            print(text)


# Invoke function from Verify Dependecies:
#check()

# Create Options:
parser = argparse.ArgumentParser(description="Scans information from a host")

parser.add_argument('-t', '--target', type=str, help='Select target to be scanned')

parser.add_argument('-p', '--port', type=str, help='Select the port to be scanned')

parser.add_argument('-c', '--command', type=str, help='Select the command line to be scanned')

parser.add_argument('--shell', type=str, dest='start/stop', help='Run commands in the Scan tool shell! Coming soon')

# Options and Arguments:
args = parser.parse_args()

# Class nmap:
class Nmap:
    def __init__(self, Ip_Adress, Door_Quatities, Nmap_Command_Line_Options):
        self.Ip_Adress = Ip_Adress
        self.Door_Quatities = Door_Quatities
        self.Nmap_Command_Line_Options = Nmap_Command_Line_Options
        self.Temporary_Records = []
        self.Nscan = nmap.PortScanner()
        self.version = '2.1'
        self.times = list(time.localtime())
        # Aqui vem a lista contendo todos os parâmetros que
        # seão executados apenas com acesso de root 'super-usuário'
        self.command_root = ['-sS', '-sU', '-O', '-PO', '-PU', '-PY', '--traceroute', '-sA', '-sW', '-sM', '-sN', '-sF', '-sX', '-sY', '-sZ', '-sO', '-f', '--badsum', '-6']
        self.command_noroot = ['-sV', '-Pn', '-A', '-v']
        self.command_all = self.command_root.append(self.command_noroot)

    def scanning(self):
        try:
            print('Starting Nscan {} ( {} ) at {}-{}-{} {}:{} -{}'.format(self.version, self.Ip_Adress, self.times[0], self.times[1], self.times[2], self.times[3], self.times[4], self.times[5]))
            # Escaner será dessa maneira, exemplo:
            # ===> (nmap vulnweb.com -p 21-22 -sS -sV -O)
            self.Nscan.scan(self.Ip_Adress, arguments="{0} -p {1}".format(self.Nmap_Command_Line_Options, self.Door_Quatities))
        except nmap.nmap.PortScannerError as error:
            print(error)


    def prints(self):
        for host in self.Nscan.all_hosts():
            self.Temporary_Records.append(self.Nscan.get_nmap_last_output())
            fileLog = open('scan.log', 'w')
            fileLog.write(self.Temporary_Records[0])
            fileLog.close()
            print(self.Nscan.command_line())
            print('\n\033[0mIp Adress: (\033[00;92m{}\033[0m), Website: (\033[00;92m{}\033[0m)'.format(host, self.Nscan[host].hostname()))
            for key in self.Nscan.analyse_nmap_xml_scan()['nmap']['scaninfo']['tcp']:
                if "osmatch" == key:
                    print('\033[0mMethod: (\033[00;92m{}\033[0m), Osmatch: (\033[00;92m{}\033[0m)'.format(self.Nscan.analyse_nmap_xml_scan()['nmap']['scaninfo']['tcp']['method'], self.Nscan[host]['osmatch'][0]['name']))
                else:
                    pass
                pass
            for key in self.Nscan[host]:
                if "osmatch" == key:
                    print('\033[0mVendor: (\033[00;92m{}\033[0m), Osfamily: (\033[00;92m{}\033[0m), Osgen: (\033[00;92m{}\033[0m)'.format(self.Nscan[host]['osmatch'][0]['osclass'][0]['vendor'], self.Nscan[host]['osmatch'][0]['osclass'][0]['osfamily'], self.Nscan[host]['osmatch'][0]['osclass'][0]['osgen']))
                    print('\033[0mTimestr: (\033[00;92m{}\033[0m), command_line: (\033[00;92m{}\033[0m)'.format(self.Nscan.scanstats()['timestr'], self.Nscan.command_line()))
                    break
                else:
                    pass
        try:
            for port in self.Nscan[host]['tcp'].keys():
                print('\n\033[0mPort: (\033[00;92m{}\033[0m), State: (\033[00;92m{}\033[0m)'.format(port, self.Nscan[host]['tcp'][port]['state']))
                print('\033[0mService: (\033[00;92m{}\033[0m), Version: (\033[00;92m{}\033[0m)'.format(self.Nscan[host]['tcp'][port]['name'], self.Nscan[host]['tcp'][port]['product']))
                print('\033[0mReason: (\033[00;92m{}\033[0m), Cpe: (\033[00;92m{}\033[0m)'.format(self.Nscan[host]['tcp'][port]['reason'], self.Nscan[host]['tcp'][port]['cpe']))
                for key in self.Nscan[host]['tcp'][port]:
                    if 'script' == key:
                        scripts = list(self.Nscan[host]['tcp'][port]['script'])
                        for scripting in scripts:
                            print('Script Exploration: {}'.format(scripting))
                    else:
                        pass
        except UnboundLocalError:
            print('Erro! Não foi possível continuar')


if not args.target and not args.port and not args.command:
    system('bash ./banner.sh')
    print("Ops! faltou parametros, tente => --help/-h para ajuda !")

else:
    Nmap_Scan = Nmap(args.target, args.port, args.command)
    Nmap_Scan.scanning()
    Nmap_Scan.prints()
