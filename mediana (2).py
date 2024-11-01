5,7,9,12,50
entrada = input()

numeros_str = ["5", "7", "9", "12", "50"]
lista = [float(x.strip()) for x in entrada.split(',')]

soma = sum(lista)

quantidade = len(lista)

media = soma / quantidade

print(f'{media:.1f}')
