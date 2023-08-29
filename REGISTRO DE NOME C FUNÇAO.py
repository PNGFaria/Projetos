#REGISTRO DE NOME E GOLS DE JOGADOR
def jogador(nome='<DESCONHECIDO>', gols=0):
    if nome == '' and gols != '':
        print(f'O jogador <DESCONHECIDO> fez {gols} gol(s).')
    elif nome == '' and gols == '':
        print('O jogador <DESCONHECIDO> fez 0 gols')
    elif gols == '':
        print(f'O jogador {nome} fez 0 gols')
    else:
        print(f'O jogador {nome} fez {gols} gol(s).')

nom = str(input('Digite o nome do jogador: '))
go = input('Digite quantos gols o jogador fez: ')
jogador(nom, go)
