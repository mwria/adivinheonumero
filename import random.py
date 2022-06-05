import random
from tkinter import N

jogar = 's'

while (jogar == 's'):
    resposta = random.randint(1,100)
    tentativa = input("Tente adivinhar o número entre 1 e 100:")
    tentativa = int(tentativa)
    contagem = 1

    while tentativa != resposta:
        if tentativa <resposta:
            print('O numero é maior.')
        if tentativa> resposta:
            print('o numero é menor.')
        tentativa = int(input("Tente adivinhar o número entre 1 e 100:"))
        contagem = contagem + 1
    print('Você acertou depois de ' + str(contagem) + ' tentativas! Parabens!')
    jogar = input('deseja continuar? digite s se sim: ')
