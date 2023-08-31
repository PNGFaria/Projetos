#VERIFICADOR DE NÚMEROS ALEATÓRIOS COM FUNÇÃO
from random import randint


def sorteia(lista):
    for c in range(0, 5):
        lista.append(randint(1, 50))


def somapar(lis):
    soma = 0
    for c in lis:
        if c % 2 == 0:
            soma = soma + c
    print(soma)


nums = list()
sorteia(nums)
print(f'Dentre os números {nums}, a soma entre os pares é: ')
somapar(nums)
