#Consulta dns de domínio, para ver para qual ip ele esta apontando#
import dns.resolver   #Biblioteca que possibilita realizar consultas de dns#

res = dns.resolver.Resolver()    #Inicializando um objeto do tipo resolver p>
alvo = "bancocn.com"            #String com o nome do dominio que vai ser ac>
resultado = res.resolve(alvo, "A")    #metodo para passar o dominio que dese>
for ip in resultado:            #Ciclo para printar todas as informacoes do >
    print(alvo, "->", ip)   #printa os resultados#