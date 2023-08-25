#verificador de idade para voto
def voto(ano):
    ano = 2023 - ano
    if ano < 16:
        print(f'Com {ano} anos, NEGADO')
    elif 16 <= ano < 18 or ano > 65:
        print(f'Com {ano} anos, Voto opcional')
    elif 18 <= ano <= 65:
        print(f'Com {ano} anos, Voto obrigatório')



idade = int(input('Digite o ano que nasceu: '))
voto(idade)
