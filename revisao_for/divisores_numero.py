n = int(input('Digite um número: '))

for cont in range (n, 0, -1):
    if n % cont == 0:
        print(f'{cont}')


