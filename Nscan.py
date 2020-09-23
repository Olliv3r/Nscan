#!/bin/env python3
# Name: Nscan
# Describe: Escaner de portas de serviços remotos
# Lisense: MIT Lisense
# Author: Olive <https://tecnospeed.000webhostapp.com/>
# Version: 2.1

# Necessary modules:
from os import system
import optparse
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
parse = optparse.OptionParser()
parse.add_option('-t', '--target', help='Select target to be scanned', dest='target', metavar='TARGET')
parse.add_option('-p', '--port', help='Select the port to be scanned', dest='port', metavar='PORT')
parse.add_option('-c', '--command', help='Select the command line to be scanned', dest='command', metavar='COMMAND_LINE')


# Options and Arguments:
(options, args) = parse.parse_args()

# Class nmap:
class Nmap:
    def __init__(self, Ip_Adress, Door_Quatities, Nmap_Command_Line_Options):
        self.Ip_Adress = Ip_Adress
        self.Door_Quatities = Door_Quatities
        self.Nmap_Command_Line_Options = Nmap_Command_Line_Options+' -p {}'.format(self.Door_Quatities)
        self.Temporary_Records = []
        self.Nscan = nmap.PortScanner()
        self.version = '2.1'
        self.times = list(time.localtime())

    def scanning(self):
        try:
            print('Starting Nscan {} ( {} ) at {}-{}-{} {}:{} -{}'.format(self.version, self.Ip_Adress, self.times[0], self.times[1], self.times[2], self.times[3], self.times[4], self.times[5]))
            self.Nscan.scan(self.Ip_Adress, arguments=self.Nmap_Command_Line_Options)
        except nmap.nmap.PortScannerError:
            print('Permissão negada! você não tem privilégio administrativo Para continuar, conceda acesso de super-usuário ao comando ou coloque o sudo antes do comando.')
            exit()

    def prints(self):
        for host in self.Nscan.all_hosts():
            self.Temporary_Records.append(self.Nscan.get_nmap_last_output())
            fileLog = open('scan.log', 'w')
            fileLog.write(self.Temporary_Records[0])
            fileLog.close()
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



# Tratar parametros, se inseridos completamentes:
if not options.target and not options.port and not options.command:
    system('bash ./banner.sh')
    print("Ops! faltou parametros, tente => --help/-h para ajuda !")
    exit(1)
else:
    if options.target:
        if options.port:
            if options.command:
                pass
            else:
                print('Ops! Faltou 1 paramêtro => "command_line"')
                exit(1)
        else:
            print('Ops! Faltou 2 parâmetros => "port" e "command_line"')
            exit(1)

    # Tratar o protocolo, se começa com 'http' ou 'https' ou 'www':
    if(options.target.lower() [0:7] == "http://" or options.target.lower()[0:8] == 'https://' or options.target.lower() [0:3] == "www"):
        print('Insira apenas o domínio, não precisa expecificar o protocolo "http" ou "https" ou "www"')
        exit(1)
    else:
        
        Nmap_Scan = Nmap(options.target, options.port, options.command)
        Nmap_Scan.scanning()
        Nmap_Scan.prints()
