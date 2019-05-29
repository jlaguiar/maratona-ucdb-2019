n = int(input())
while n != 0:
    qtd_diamantes = 0
    counter = 0
    mina = input()
    for i in range(len(mina)):
        if (mina[i] == "<"):
            counter += 1

        elif (mina[i] == ">"):
            counter -= 1
            if (counter >= 0):
                qtd_diamantes += 1
            else:
                counter = 0

    print(qtd_diamantes)
    n -= 1