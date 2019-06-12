#!/usr/bin/env python3
# Autor: olive
# Nome: Nscan
# Descrição: simples scanner de portas.
# Versão: beta. v0.1
# mais sobre o autor:
# ===================================================
# = Site: https://olivetech933842787.wordpress.com
# = Pagina: https://facebook.com/oliveobom
# = Canal yt: https://www.youtube.com/channel/UC6gMF4GxvOwuC7q7biSKFDA
# ====================================================


# importação das bibliotecas necessárias para funcionamento correto
import nmap
import os
import subprocess
import time
import sys

# Criando objeto de scan
n = nmap.PortScanner()
# Criando objeto de data recente
data = time.localtime()
H = time.gmtime()

if len(sys.argv) < 4:
    subprocess.run('clear')
    print('Usage Nscan.py: \n\n\n./Nscan.py [target] [portas] [comando linha]')
    print("\n\nExemplo Nscan.py: \n\n\n./Nscan.py testphp.vulnweb.com 21-22 '-sV'\n")
    print('\n\nCopyright Nscan.py')
    exit()

# Criando Class (nmap)
class nmap:
    # Inicializando a função de inicialização principal (__init_)
    # passando 3 atributos como argumentos para a classe
    # nmap (target, porta_inicial, porta_final) 
    # e um atributo principal de scan (scanner)
    def __init__(scanner, target, portas, comando_linha):
        # Começando a criar os atributos (variaveis
        # de dentro da classe)
        scanner.target = target
        scanner.portas = portas
        scanner.comando_linha = comando_linha
        
        # limpar a tela antes de execução do programa
        subprocess.run('clear')
        # Exibi o banner do programa
        os.system("sh banner.sh")
        # esperar 1 segundo antes de executar o proximo passo
        time.sleep(1)


    # Criando uma função que irar fazer o scan dos dados
    # passados como argumentos (parametros= 
    # target,porta_inicial, porta_final)
    def scan(scanner):
        print ("\n\033[01;92mScan iniciado por, favor aguarde o termino do scan...\n\nHost:> \033[01;93m{}\n\033[01;92mPortas:> \033[01;93m[{}] \n\033[01;92mComando linha: \033[01;93m{}\033[0m\n".format(scanner.target, scanner.portas, scanner.comando_linha))
        # scan em andamento
        n.scan(scanner.target, scanner.portas, scanner.comando_linha)
    # criando outra função que mostrará o resultado do scan feito
    def imprime_resultado(scanner):
        # Exibi uma menssagem com texto 'Resultados'
        print("\033[01;96mResultados\033[0m\n")
        # para cada host que estiver na lista n.all_hosts()
        # faça, 
        for host in n.all_hosts():
            # imprima o ip do host, e imprima o próprio host
            print("\033[01;93mIP: \033[01;91m{}, \033[01;93mSite: \033[01;91m{}\033[0m".format(host, n[host].hostname()))
            # para cada protocolo que estiver na 
            # lista n[host].all_protocols(), faça
            for proto in n[host].all_protocols():
                # imprima na tela o protocolo apenas
                print("\033[01;93mProtocolo: \033[01;91m{}\033[0m".format(proto))
                # imprima na tela o estado apenas
                print("\033[01;93mState: \033[01;91m{}\033[0m".format(n[host].state()))
                
                # pasando para variavel (lport) todas as chaves
                # do dicionario n[host][proto].keys()
                lport = n[host][proto].keys()
                # convertendo o dicionario lport em lista
                lport = list(lport)
                # colocando a lista em ordem
                lport.sort()
                
                # para cada porta que estiver na lista lport
                # faça,
                for porta in lport:
                    # imprima a porta e o estado desta porta
                    # se estar aberta ou fechada (rodando
                    # algum serviço no host)
                    print("\033[01;93mPorta: \033[01;91m{}, \033[01;93mEstado: \033[01;91m{}\033[0m".format(porta, n[host][proto][porta]['state']))
                    # Deixar uma linha em branco
                    print ("")
                    # exibi um texto de 'scanner completo'
                    # data recente do scan
                print("\033[01;94mScanner completo. \ndata recente: {}/{}/{} : hora: {} Minuto: {}\033[0m".format(data[2], data[1], data[0], data[3], H[4]))


# passando a classe para uma variavel (scan_finalizado)
scan_finalizado = nmap(sys.argv[1], sys.argv[2],sys.argv[3])
# chamando a função scan()
scan_finalizado.scan()
# chamando a função imprime_resultado()
scan_finalizado.imprime_resultado()

# Copyright olive
