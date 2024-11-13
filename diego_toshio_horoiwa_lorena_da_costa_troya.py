dias= int(input('Insira a quantidade de dias: '))
maior = 0
menor = 0
media = 0
soma_de_consumo = 0
cumpriram = 0
nao_cumpriram = 0
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

    if consumo >= meta:
        cumpriram += 1
    else:
        nao_cumpriram += 1


media = soma_de_consumo/dias

if cumpriram == dias:
    print(f'Parabéns! Todos os dias cumpriram a meta de consumo sustentável.')

elif nao_cumpriram == dias:
    print(f'Infelizmente, nenhum dia cumpriu a meta de consumo sustentável.')

else:
    print(f'{cumpriram} dias cumpriram a meta e {nao_cumpriram} dias não cumpriram a meta.')

print(f'A média de consumo foi de {media:.2f} kWh. O maior consumo foi de {maior} kWh e o menor consumo foi de {menor} kWh')
