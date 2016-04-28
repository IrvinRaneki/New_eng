#########=====servpy=====##########
#!/user/bin/python
import socket

import time

##################################################################
#             funcao conect: aguarda o recebimento da msg        #
##################################################################
def conect(addr, recebe):
    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #->mecanismos de recepcao de conexao - argv[1-familia do protocolo() 2-tipo de envio(tcp/ip)]
    serv_socket.bind(addr)
    #->mostra qual o ip e porta o servidor devem aguardar a conexao
    while True:
        recebe, cliente = serv_socket.recvfrom(1024)
        #->apos conexao ha o aguardo de dado enviado pela rede de ate 1024 Bytes (1 argv -> tamanho do buffer)
        print "mensagem recebida: "+ recebe
    serv_socket.close()

##################################################################
#                           funcao main                          #
##################################################################
def main():
    recebe=''
    host = ''
    port = 8888
    addr = (host, port)

    conect(addr, recebe)

if __name__ == '__main__':
    main()
