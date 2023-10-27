from random import randint

def sortear(lista):
    for cont in range(1, 11):
        lista.append(randint(1,100))
    
    print(f'Lista gerada: {lista}')

def conta_par(lista):
    totpar = 0
    for cont in range(0, 10):
        if lista [cont] % 2 == 0:
            totpar += 1
    print(f'Total de pares: {totpar}')

numeros = []
sortear(numeros)
conta_par(numeros)
