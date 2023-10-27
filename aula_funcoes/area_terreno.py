def calcula_area(largura, comprimento):
    return largura * comprimento

largura = float(input('Digite a largura do retângulo: '))
comprimento = float(input('Digite o comprimento do retângulo: '))


print(f'A área é: {calcula_area(largura, comprimento):.2f}')