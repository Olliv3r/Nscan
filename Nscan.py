#!/usr/bin/env python3
# nome: Nscan
# descrição: Simples scanner de portas e serviços
# versao: beta: v0.2

# importação de bibliotecas necessárias
import optparse
import nmap
import time
import subprocess
import os

# função de verificação de dependencias
def ch():
    if os.path.exists('/data/data/com.termux/files/usr/bin/python') == False :
        if os.path.exists('/data/data/com.termux/files/usr/bin/nmap') == False :
            if os.path.exists('/data/data/com.termux/files/usr/lib/python3.7/nmap') == False :
                os.system('bash ./install.sh')
            else:
                return 0
        else:
            return 0
    else:
        return 0

# chamando função de verificação
ch()

# criando objetos (objetos de=[opçôes, Scan, data & hora & minutos)
parse = optparse.OptionParser()
Nscan = nmap.PortScanner()
data = time.localtime()
H = time.gmtime()

# criando opçoes
parse.add_option('-?', '--all', action='help', help='Ajuda', dest='ajuda', metavar='AJUDA')
parse.add_option('-t', '--target', help='Seleciona o alvo', dest='target', metavar='TARGET')
parse.add_option('-p', '--port', help='Seleciona a porta expecifica pro alvo', dest='port', metavar='PORT')
parse.add_option('-c', '--comando', help='Seleciona um tipo de scan expecifica pro alvo [service/version/detection system OS', dest='comando', metavar='COMANDO')

# passando os argumentos e opçôes para as variáveis (args & options)
(args, options) = parse.parse_args()

# criando classe (Nmap)
class Nmap:
    def __init__(olive, target, port, comando):
        olive.target = target
        olive.port = port
        olive.comando = comando

    # função de scan
    def scan(olive):
        subprocess.run('clear')
        print('\033[01;94mScanning....\n')
        time.sleep(1)
        print('\n\t\t\t\033[01;96;44mBy: olive\033[0m')
        print('\n\033[01;92mScan em execução, por favor aguarde o processo de scan terminar\n')
        print('\n\033[01;94mDados passados na entrada\n')
        print('\033[01;92m-'*25)
        print('\033[01;96mHost: \033[01;91m{}\n\033[01;96mPorta: \033[01;91m{}\n\033[01;96mComando linha: \033[01;91mnmap {}\n'.format(olive.target, olive.port, olive.comando))
        print('\033[01;92m-'*25)
        time.sleep(2)
        Nscan.scan(olive.target, olive.port, olive.comando)
    
    # função de exibi o resultado do scan
    def imprime(olive):
        print('\n\033[01;96mResultados do scan\n')
        for host in Nscan.all_hosts():
            print('\n\033[01;96mIP: \033[01;92m[\033[01;91m{}\033[01;92m], \033[01;96msite: \033[01;92m[\033[01;91m{}\033[01;92m]\n'.format(host, Nscan[host].hostname()))
            for proto in Nscan[host].all_protocols():
                print('\033[01;96mProtocolo: \033[01;92m[\033[01;91m{}\033[01;92m]\n'.format(proto))
                print('\033[01;96mState: \033[01;92m[\033[01;91m{}\033[01;92m]\n'.format(Nscan[host].state()))

                lport = Nscan[host][proto].keys()
                lport = list(lport)
                lport.sort()

                for porta in lport:
                    print('\033[01;96mPorta: \033[01;92m[\033[01;91m{}\033[01;92m], \033[01;96mEstado: \033[01;92m[\033[01;91m{}\033[01;92m]\n'.format(porta, Nscan[host][proto][porta]['state']))



# verificando se Nscan receberar algum parametro
if args.target == None:
    subprocess.run('clear')
    os.system('bash banner.sh')

    print('\n\n\033[01;92;41mInvalid\033[0m \033[01;96m[\033[01;92m!\033[01;96m] \033[0m -h/--help\n\n')
elif args.target:
    if args.target.lower() [0] == "h":
        print("\n\nInsira o site sem o 'HTTP' ou 'HTTPS'\nExemplo: testphp.vulnweb.com\n\n")
    elif args.target.lower() [0] != "http" or "https":
        if args.target:
            if args.port:
                if args.comando:

                    # excessão de parametros invalidos
                    try:

                        Nmap_Res = Nmap(args.target, args.port, args.comando)
                        # excessão de parada forçada
                        try:
                            Nmap_Res.scan()
                            Nmap_Res.imprime()
                            print("\n\033[01;94mScanner completo. \ndata recente: {}/{}/{} : hora: {} Minuto: {}\033[0m".format(data[2], data[1], data[0], data[3], H[4]))
                        except KeyboardInterrupt:
                            print("\nParada forçada\n")
                            exit()
                            # fim da excessão da parada forçada

                    except nmap.nmap.PortScannerError:
                        print('\nPermissão negada. Este parâmetro requer, permissão de ROOT. use o sudo para prosseguir\n')

                else:
                    print('Insira os parametros')
            else:
                print('Insira a porta')
