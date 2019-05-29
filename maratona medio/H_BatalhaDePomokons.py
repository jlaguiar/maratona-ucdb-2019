t = int(input())
while t != 0:
    b = int(input())
    valores = input().split()
    valor_golpe_1 = (int(valores[0]) + int(valores[1])) / 2
    if (int(valores[2]) % 2 == 0):
        valor_golpe_1 = valor_golpe_1 + b

    valores = input().split()
    valor_golpe_2 = (int(valores[0]) + int(valores[1])) / 2
    if (int(valores[2]) % 2 == 0):
        valor_golpe_2 = valor_golpe_2 + b

    if (valor_golpe_1 > valor_golpe_2):
        print("Dabriel")
    elif (valor_golpe_2 > valor_golpe_1):
        print("Guarte")
    else:
        print("Empate")

    t -= 1