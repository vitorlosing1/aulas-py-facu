contdiv = 0

n = int (input('Digite um número:'))

for cont in range (1, n + 1):
    
    if n % cont == 0:
        contdiv += 1

if contdiv == 2 and n != 2:
    print('É número primo')

else:
    print('Não é número primo')