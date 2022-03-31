import socket   #Biblioteca pythom que permite o programa fazer conexões com servidores web#

#Como se fosse inicializar um objeto/socket.AF_INET->Familia do socket/socket.SOCK_STREAM->Tipo do socket/socket do protocolo tcp ip#
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	#Client recebe um objeto socket, que é o objeto que vai realizar as ações conexões com o servidor e fazer as devidas chamadas#
client.connect(("bancocn.com", 80))	#metodo de conexão com o servidor/ host&porta#
client.send(b"hello world!")	#Envio dados para a conexão/ b-> tranforma o envio em bytes#
resposta = client.recv(1024)	#metodo para receber dados da conexão(como argumento se passa a qunatidade de bytes que se quê receber)#
print(resposta.decode()) 	#printa na tela a resposta/.decode->metodo para tranformar o conteúdo em string#

#Conexão com servidor bancocn.com#
