#variáveis
import random

jogador = ''
computador = ''
escolhas = ['papel', 'pedra', 'tesoura']
vjogador = 0
vcomputador = 0
empates = 0
x = 0

while True:
    print('Jogo Jokenpô')
    print('\n')
    print('Opções:')
    print('Pedra')
    print('Tesoura')
    print('Papel')
    print('\n')
    jogador = input('Entre com sua opção: ')
    while True:
        if jogador == 'papel' or jogador == 'Papel' or jogador =='Pedra' or jogador == 'pedra' or jogador =='Tesoura' or jogador == 'tesoura': break
        else:
            print('Tente novamente!')
            jogador = input('sua opção? ')
    computador = random.choice(escolhas)
    print(f'JOGADOR = {jogador} | COMPUTADOR = {computador}')
    if jogador == computador:
        print('Empate!')
        empates += 1
    elif jogador == 'papel' and computador == 'pedra' or jogador == 'tesoura' and computador == 'papel' or jogador == 'pedra' and computador == 'tesoura':
        print('Vitória!')
        vjogador += 1
    else:
        print('Derrota!')
        vcomputador +=1
    
    print(f'VITORIAS JOGADOR = {vjogador} | VITORIAS COMPUTADOR {vcomputador} | EMPATES {empates}')
    pergunta = input('Deseja continuar a jogar?  S/N ').upper()
    if pergunta == 'N':
        break