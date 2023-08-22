#este programa simula um caixa eletrônico
valor = int(input('Qual valor voce deseja sacar? '))
total = valor
'''variável ced representa a cédula de maior valor disponível, sendo o parâmetro inicial. No sistema consta cedulas de 50, 
20, 10 e 1, mas pode ser de qualquer valor'''
ced = 50
totalced = 0

while True:
    if total >= ced:
        total = total - ced
        totalced = totalced + 1
        #este primeiro if irá fazer a contagem de notas pelo valor inputado pelo usuario, usando o valor da cedula inicial como parametro

    else:
        if totalced > 0:
            print(f'Total de {totalced} cedulas de {ced}')
        #quando o if é finalizado, ele fara o print da impressao de cedulas do valor de 50
        #em seguida ele fara a verificaçao e atualização do valor da variavel da cedula para q outras notas de valor menor possam ser impressas, caso necessario
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1

        #sempre que houver uma troca de valor da cedula, o total de cedulas sera zerado para que a quantidade seja compativel com o novo valor
        totalced = 0
        if total == 0:
            break
print('Fim.')
