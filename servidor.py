# -*- coding: utf-8 -*-
import socket
import math

def main():
    host = 'localhost'
    porta = 1234

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind((host,porta))

    print('Esperando cliente...')
    message, clientAddress = serverSocket.recvfrom(2048)
    print('Conexão de: ', clientAddress)

    comandos = message.decode('utf-8').split('\\n')

    for linha in comandos:
        comando = linha.split(' ')
        mensagem_retorno = ''
        if (comando[0] == 'soma' and len(comando) == 3): 
            mensagem_retorno += somar(int(comando[1]), int(comando[2]))
        elif (comando[0] == 'subtrair' and len(comando) == 3):
            mensagem_retorno += subtrair(int(comando[1]), int(comando[2]))
        elif (comando[0] == 'multiplicar' and len(comando) == 3):
            mensagem_retorno += multiplicar(int(comando[1]), int(comando[2]))
        elif (comando[0] == 'dividir' and len(comando) == 3):
            mensagem_retorno += dividir(int(comando[1]), int(comando[2]))
        elif (comando[0] == 'raiz_quadrada' and len(comando) == 2):
            mensagem_retorno += raiz_quadrada(int(comando[1]))
        else:
            mensagem_retorno += 'Mensagem inválida'
        serverSocket.sendto(mensagem_retorno.encode('utf-8'), clientAddress)
    serverSocket.sendto(''.encode(('utf-8')), clientAddress)


def somar(a, b):
    return str(a) + ' + ' + str(b) + ' = ' + str(a + b)

def subtrair(a, b):
    return str(a) + ' - ' + str(b) + ' = ' + str(a - b)

def multiplicar(a, b):
    return str(a) + ' * ' + str(b) + ' = ' + str(a * b)

def dividir(a, b):
    return str(a) + ' / ' + str(b) + ' = ' + str(a / b)

def raiz_quadrada(a):
    return 'Raiz quadrada de ' + str(a) + ' = ' + str(math.sqrt(a))

if __name__ == "__main__":
    main()
