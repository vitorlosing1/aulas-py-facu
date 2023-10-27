par = 0
impar = 0

for i in range(1, 11):
    n = int(input('Digite um número: '))

    if n % 2 == 0:
        par += 1

    else:
        impar += 1

print(f'O total de pares são {par} e o total de impares são {impar}')