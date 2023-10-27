def verifica (lista):
    while True:
        n = int(input('Digite um número: '))
        lista.append(n)

        resp = str(input('Deseja continuar(S/N): ')).upper()

        if resp in 'Nn':
            break

    print(f'Lista Digitada: {lista}')
    print(f'Maior número: {max(lista)}')
    print(f'Menor número: {min(lista)}')
    
numeros = []
verifica(numeros)

