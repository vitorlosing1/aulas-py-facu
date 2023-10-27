def verifica_idade(idade):
    if idade < 16:
        print(f'Aos {idade} anos o voto não é obrigatório')

    elif idade >= 18:
        print(f'Aos {idade} anos o voto é obrigatório')

    else:
        print(f'Aos {idade} anos o voto é opcional')

idade = int(input('Digite sua idade: '))

verifica_idade(idade)