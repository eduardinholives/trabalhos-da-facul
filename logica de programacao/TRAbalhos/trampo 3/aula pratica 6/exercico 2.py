import random


def valida_int(pergunta,min,max):
    x = int(input(pergunta))
    while ((x< min) or (x>max)):
        x = int(input(pergunta))
    return x

def vencedor(jogador1,jogador2):
    global empate, v1 , v2
    if jogador1 == 1:
        if jogador2 == 1:
            empate +=1
        elif jogador2 == 2:
            v1 +=1
        elif jogador2 == 3:
            v2 +=1
    if jogador1 == 2:
        if jogador2 == 1:
            v2 +=1
        elif jogador2 == 2:
            empate +=1
        elif jogador2 == 3:
            v1 +=1
    if jogador1 == 3:
        if jogador2 == 1:
            v1 +=1
        elif jogador2 == 2:
            v2 +=1
        elif jogador2 == 3:
            empate +=1
    resultados = [v1,v2,empate]
    return resultados
print('JOKENPO')
print('1 - PEDRA')
print('2 - TESOURA')
print('3 - PAPEL')

resultados = []
JOGADAS = []
v1 = 0
v2 = 0
empate = 0

while True:
    j1 = valida_int('escolha sua jogada:' ,0,3)
    if not j1:
        break
    j2 = random.randint(1,3)
    JOGADAS.append([j1, j2])
    resultados = vencedor(j1,j2)
    #resultados = vencedor(j1,j2)

    for jogada in JOGADAS:
        for dado in jogada:
            print(dado, end= " ")
        print()

print('numero de vitorias do jogador 1: {}'.format(resultados[0]))
print('numero de vitorias do jogador 2: {}'.format(resultados[1]))
print('numero de empates: {}'.format(resultados[2]))
