#Este programa faz uma verificação de preços de produtos
cont = baratop = caro = preco = contp = soma = 0
nome = ''
parada = ''

while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    cont = cont + 1
    soma = soma + preco
    #neste primeiro bloco há um contador para parametro de preços mais altos e baixos junto com a variavel de soma.

    if cont == 1:
        baratop = preco
        baraton = nome
        #aqui como é o primeiro produto, como indicado pelo contador, ele sera o mais barato.
    else:
        if preco < baratop:
            baraton = nome
        #este else irá a partir do segundo produto, e ele irá verificar se seu preço é menor que o do produto mais barato.
        #caso seja, o nome na variavel sera substituido por ele
    if preco > 1000:
        contp = contp + 1
    #contador de quantos produtos custam mais que 1000.

    parada = str(input('Deseja continuar? '))
    while parada not in 'sn':
        parada = str(input('Código inválido. Deseja continuar? '))
    if parada == 'n':
        break

print(f'O total gasto é {soma}, {contp} produto(s) custa(m) mais que 1000 reais e o produto mais barato é o {baraton}')