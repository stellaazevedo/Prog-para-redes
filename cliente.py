# -*- coding: utf-8 -*-
import socket
def main():
    host = 'localhost'
    porta = 1234

    clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    message = input('Operação: ')
    byte_msg = message.encode('utf-8')

    clientSocket.sendto(byte_msg, (host,porta))

    while True:
        mensagem_servidor, serverAddress = clientSocket.recvfrom(2048)
        retorno = mensagem_servidor.decode('utf-8')
        if retorno == '':
            break
        print(retorno)
    clientSocket.close()

if __name__ == "__main__":
    main()