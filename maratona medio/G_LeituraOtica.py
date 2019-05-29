_input = int(input())
while _input != 0:
    while _input != 0:
        letra = 0
        alternativas = input().split()
        for i in range(5):
            if (int(alternativas[i]) < 128):
                if (letra != 0):
                    letra = 0
                    break

                letra = i + 1

        if (letra == 0):
            print("*")
        else:
            if (letra == 1):
                print("A")
            elif (letra == 2):
                print("B")
            elif (letra == 3):
                print("C")
            elif (letra == 4):
                print("D")
            elif (letra == 5):
                print("E")
            else:
                print("*")

        _input -= 1

    _input = int(input())