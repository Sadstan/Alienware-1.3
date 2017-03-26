#ecoding:utf-8
import socket
import time
from os import system

def banner():
	print"""

 █████╗ ██╗     ██╗███████╗███╗   ██╗██╗    ██╗ █████╗ ██████╗ ███████╗                             
██╔══██╗██║     ██║██╔════╝████╗  ██║██║    ██║██╔══██╗██╔══██╗██╔════╝                             
███████║██║     ██║█████╗  ██╔██╗ ██║██║ █╗ ██║███████║██████╔╝█████╗                               
██╔══██║██║     ██║██╔══╝  ██║╚██╗██║██║███╗██║██╔══██║██╔══██╗██╔══╝                               
██║  ██║███████╗██║███████╗██║ ╚████║╚███╔███╔╝██║  ██║██║  ██║███████╗                             
╚═╝  ╚═╝╚══════╝╚═╝╚══════╝╚═╝  ╚═══╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝                             
                                                                                                    
██████╗  ██████╗ ██████╗ ████████╗███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗██╗███╗   ██╗ ██████╗ 
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██║████╗  ██║██╔════╝ 
██████╔╝██║   ██║██████╔╝   ██║   ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║██║██╔██╗ ██║██║  ███╗
██╔═══╝ ██║   ██║██╔══██╗   ██║   ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██║██║╚██╗██║██║   ██║
██║     ╚██████╔╝██║  ██║   ██║   ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║██║██║ ╚████║╚██████╔╝
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 

	\033[34m[*]\033[0;0m \033[33mCODED BY SADSTAN\033[0;0m
	\033[34m[*]\033[0;0m \033[33m1.3 VERSION\033[0;0m
	\033[34m[*]\033[0;0m \033[33mNEW DESIGN033\033[0;0m
	\033[34m[*]\033[0;0m \033[33mwww.github.com/sadstan\033[0;0m
	"""
banner()

def digite_continue_Y():
    digite_continue = raw_input("\033[34mContinue?...\033[0;0m \033[33m[Y / n] \033[0;0m")

    if digite_continue == '-h':
        ############################################
        # Esse é o centro de ajudas e suas funcoes #
        ############################################
        print"""
                    \033[31m ________________________\033[0;0m
                    \033[31m|                        |\033[0;0m

                            \033[42;1;33m => Help <=\033[0;0m

                    \033[31m|________________________|\033[0;0m
                \033[37m
                ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                + #Codado by SadStan                                                             +
                + #Greetz: Diogo Makaveli - Júlia Siilva - Livia Guillens OpCoder - Luis Henrique+
                + #AlienWare  PortScanning                                                       +
                ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

                ++++++++++++++++++++++++++++
                + #exit   [para sair]      +
                + #-h     [para help]      +
                ++++++++++++++++++++++++++++
                \033[0;0m
                \033[31m=================================================\033[0;0m
        """
    elif digite_continue == 'exit':
        print("\033[31mSaindo...\033[0;0m")
        system("reset")
        exit()

    elif digite_continue == "Y":
    	time.sleep(5)
        print("\033[34m[*]\033[0;0m Carregando")

    elif digite_continue == "N":
        exit()
        system("reset")
    else:
        print"Opcao invalida"

print("\n")

################################
# Fim centro de ajudas         #
################################

digite_continue_Y() #chama ajuda

ip = raw_input("\033[34m[+]\033[0;0m \033[37mIp ou endereco:\033[0;0m ")

if ip == "exit":
    print("\033[37mSaindo...\033[0;0m")
    system("reset")
    exit()

elif ip == '-h':
    print"""

    \033[31m ________________________\033[0;0m
     \033[31m|                        |\033[0;0m

      \033[42;1;33m => Help <=\033[0;0m

        \033[31m|________________________|\033[0;0m
         \033[37m
            ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            + #Codado by SadStan                                                             +
            + #Greetz: Diogo Makaveli - Júlia Siilva - Livia Guillens OpCoder - Luis Henrique+
            + #AlienWare  PortScanning                                                       +
            ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            ++++++++++++++++++++++++++++
            + #exit   [para sair]      +
            + #-h     [para help]      +
            ++++++++++++++++++++++++++++
            \033[0;0m
    \033[31m=================================================\033[0;0m
    """
    print("\033[37mPor favor reinicie o script\033[0;0m")
    exit()

ports = []
count = 1
e = 0

quantidade = raw_input("\033[34m[+]\033[0;0m \033[37mDigite a quantidade de portas:\033[0;0m ")

if str(quantidade) == 'exit':
    print("\033[37mSaindo...\033[0;0m")
    system("reset")
    exit()

elif str(quantidade) == '-h':
    print"""

                \033[31m ________________________\033[0;0m
                \033[31m|                        |\033[0;0m

                        \033[42;1;33m => Help <=\033[0;0m

                \033[31m|________________________|\033[0;0m
            \033[37m
            ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            + #Codado by SadStan                                                             +
            + #Greetz: Diogo Makaveli - Júlia Siilva - Livia Guillens OpCoder - Luis Henrique+
            + #AlienWare  PortScanning                                                       +
            ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            ++++++++++++++++++++++++++++
            + #exit   [para sair]      +
            + #-h     [para help]      +
            ++++++++++++++++++++++++++++
            \033[0;0m

            Por favor, reinicie o script!

\033[31m=================================================\033[0;0m
    """
    exit()

while count <= int(quantidade):
    digite_a_porta = ports.append(int(raw_input("\033[34m[*]\033[0;0m \033[37mDigite a porta\033[0;0m "+str(count) +'\033[37m:\033[0;0m')))
    count +=1

digite_a_porta = raw_input("\033[34mContinue?...\033[0;0m \033[33m[Y / n] \033[0;0m")

if digite_a_porta == "exit":
    print("Saindo...")
    system("reset")
    exit()

elif digite_a_porta =="Y":
    print"\033[31m[+]\033[0;0m \033[32mCarregando \033[31m[+]\n\033[0;0m"
    system("reset")

elif digite_a_porta == '-h':
    print"""

                \033[31m ________________________\033[0;0m
                \033[31m|                        |\033[0;0m

                        \033[42;1;33m => Help <=\033[0;0m

                \033[31m|________________________|\033[0;0m
            \033[37m
            ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            + #Codado by SadStan                                                             +
            + #Greetz: Diogo Makaveli - Júlia Siilva - Livia Guillens OpCoder - Luis Henrique+
            + #AlienWare  PortScanning                                                       +
            ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            ++++++++++++++++++++++++++++
            + #exit   [para sair]      +
            + #-h     [para help]      +
            ++++++++++++++++++++++++++++
            \033[0;0mn
\033[31m=================================================\033[0;0m
       """
else:
    print("\n")
    print"\033[34m[+]\033[0;0m \033[32mCarregando \033[31m[+]\033[0;0m"
for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.15)
    code = client.connect_ex((ip, port))

    if code == 0:
        print("\n")
        print str("\033[37m \033[34m[*]\033[0;0m => Porta\033[0;0m")
        print str(port) +" \033[42;1;33m[Aberta]\033[0;0m "
    else:
        print("\n")
        print str("\033[37m \033[34m[*]\033[0;0m => Porta\033[0;0m")
        print str(port) +" \033[41;1;33m[Fechada]\033[0;0m"
print("\n")
print("O SCAN FOI FINALIZADO !")
print("O SCAN FOI FINALIZADO !")
print("O SCAN FOI FINALIZADO !")
print("O SCAN FOI FINALIZADO !")
print("O SCAN FOI FINALIZADO !")
print"""

                \033[31m _________________________\033[0;0m
                \033[31m|                         |\033[0;0m

                    \033[42;1;33m => PRESS EXIT <=\033[0;0m

                \033[31m|_________________________|\033[0;0m
"""
sair = raw_input("\033[37mDigite\033[0;0m \033[31mexit\033[0;0m \033[37mpara finalizar o script! =>\033[0;0m ")

if sair == 'exit':
    print("\033[37mFinalizando...\033[0;0m")
    system("reset")
    exit()

else:
    print("\033[37mOpcao invalida\033[0;0m")
