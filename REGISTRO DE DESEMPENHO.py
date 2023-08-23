#este codigo faz um registro e analisa o desempenho de jogadores em partidas de futebol
jogadores = dict()
gols = list()
tudo = list()

while True:
    partidas = 0
    jogadores.clear()
    jogadores['Nome'] = str(input('Digite o nome do jogador: '))
    jogadorespa = int(input('Quantas partidas ele jogou? '))
    gols.clear()

    for c in range(0, jogadorespa):
        gols.append(int(input(f'Quantos gols ele fez na partida {c+1}? ')))
        partidas += 1
    jogadores['partidas'] = partidas
    jogadores['gols'] = gols[:]
    jogadores['total'] = sum(gols)
    jogadores['media'] = round(sum(gols)/partidas, 1)
    tudo.append(jogadores.copy())

    condi = str(input('Deseja continuar? ')).lower().strip()[0]
    if condi == 'n':
        break

print(f'Código| Nome   |  Partidas    |      Gols    |   Soma de gols  |  Media de gols')
for p, v in enumerate(tudo):
    print(f'{p:>3}', end='   ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

while True:
    ficha = int(input('Deseja ver o rendimento de qual jogador? (999 para encerrar) '))
    if ficha == 999:
        break
    if ficha > len(tudo):
        print('Jogador inexistente')
    else:
        print(f'Ficha do jogador {tudo[ficha]["Nome"]}')
        print(f'O jogador {tudo[ficha]["Nome"]} fez {tudo[ficha]["total"]} gols em {tudo[ficha]["partidas"]} partidas, formando a média de {tudo[ficha]["media"]} gols por partida')

print('Programa finalizado.')
