#Testa se a a porta existe ou não, atravez do port scan#
import socket	#Biblioteca pythom que permite o programa fazer conexões com servidores web#

ports = [21,22,80,443,445,3306,25] 	#vetor de portas para testar se estão abertas atravez do portscan#

for port in ports:		#bloco de repetição para testar todas as portas do vetor ports
	   #Como se fosse inicializar um objeto/socket.AF_INET->Familia do socket/socket.SOCK_STREAM->Tipo do socket/socket do protocolo tcp ip#
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		#Client recebe um objeto socket, que é o objeto que vai realizar as ações conexões com o servidor e fazer as devidas chamadas#

        client.settimeout(0.1)		#seta o time de 100 ms para realizar a conexão se demorar mais que isso a porta é dada como fechada#
        code = client.connect_ex(("bancocn.com", port))	#_ex->Retorna um inteiro/ inteiro = 0 conexão bem sucedida, inteiro != 0 conexão não efetuadaimport socket#

        if code == 0:
                print(port, "OPEN")		#Escreve na tela a porta e se ela estiver aberta#
        else:
                print(port, "CLOSED")		#Escreve na tela a porta e se ela estiver fechada#
