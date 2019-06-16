# Nscan
Scanner simples de portas, versão beta. Mais recursos serão adicionados ao programa


### Opçåoes de uso

Usage: Nscan.py [options]
                                                                      Options:                                                                -h, --help            show this help message and exit

  -?, --all             Ajuda

  -t TARGET, --target=TARGET
                        Seleciona o alvo

  -p PORT, --port=PORT  Seleciona a porta expecifica pro alvo

  -c COMANDO, --comando=COMANDO
                        Seleciona um tipo de scan expecifica pro alvo
                        [service/version/detection system OS




# Cada opcão

-h, --help 	exibe uma ajuda simples
-?, -all 	exibe uma ajuda simples
-t, --target 	Seta um IP ou site a ser escaneado
-p, --port 	seta uma ou mais portas expecificas
-c, --comando	Seta um tipo de scanner (Service/Version/detection de sistemas operacionais



# Exemplos

./Nscan.py --target=testphp.vulnweb.com --port=21 --comando=-A
./Nscan.py --target=testphp.vulnweb.com --port=21-443 --comando=-sS -sV -A


Copyright © Nscan 2019
