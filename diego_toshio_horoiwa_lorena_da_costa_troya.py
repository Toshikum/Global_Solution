dias= int(input('Insira a quantidade de dias: '))
maior = 0
menor = 0
media = 0
soma_de_consumo = 0
meta = 150

for d in range (1, dias + 1):

    consumo = float(input(f'Insira o consumo do dia {d} : '))

    soma_de_consumo += consumo

    if d == 1:
        maior = consumo
        menor = consumo
    else:
        if consumo > maior:
            maior = consumo
        if consumo < menor:
            menor = consumo

media = soma_de_consumo/dias

print(f'A média de consumo foi de {media:.2f} kWh. O maior consumo foi de {maior} kWh e o menor consumo foi de {menor} kWh')
