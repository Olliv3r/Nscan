# Nscan
Scanner simples de portas, versão beta. Mais recursos serão adicionados ao programa


Screentshot 01:
---
Banner -
![Image description](https://github.com/Olliv3r/Nscan/blob/master/.src/.images/banner.png)

Screentshot 02:
---
Options -
![Image description](https://github.com/Olliv3r/Nscan/blob/master/.src/.images/options.png)

Screentshot 03:
---
Command line -
![Image description](https://github.com/Olliv3r/Nscan/blob/master/.src/.images/command_line.png)

Screentshot 04:
---
Result scan -
![Image description](https://github.com/Olliv3r/Nscan/blob/master/.src/.images/result_scan.png)

### Opçåoes de uso

Usage: Nscan.py [options]
                                                                      Options:                                                                -h, --help            show this help message and exit

  -t TARGET, --target=TARGET
                        Seleciona o alvo

  -p PORT, --port=PORT  Seleciona a porta expecifica pro alvo

  -c COMMAND, --command=COMMAND
                        Seleciona um tipo de scan expecifica pro alvo
                        [service/version/detection system OS




# Cada opcão

-h, --help 	exibe uma ajuda simples
-?, -all 	exibe uma ajuda simples
-t, --target 	Seta um IP ou site a ser escaneado
-p, --port 	seta uma ou mais portas expecificas
-c, --command	Seta um tipo de scanner (Service/Version/detection de sistemas operacionais



# Exemplos

./Nscan.py --target=testphp.vulnweb.com --port=21 --command=-A
./Nscan.py --target=testphp.vulnweb.com --port=21-443 --command='-sS -sV -A'


Copyright © Nscan 2020
