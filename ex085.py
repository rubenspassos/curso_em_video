pares = []
impares = []
numeral = []
for cont in range(0,7):
    num = (int(input("Digite um valor: ")))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
numeral.append(pares)
numeral.append(impares)
print(f'Os nuemros digitados foram {numeral}')
(numeral)[0].sort()
print(f'Os Valores pares foram {numeral[0]}')
numeral[1].sort()
print(f'Os Valores impares foram {numeral[1]}')