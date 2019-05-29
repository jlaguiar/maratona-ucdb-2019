_input = input()
while _input != '0':
    _input = _input.split()
    res = int(int(_input[0]) * int(_input[1]) * int(_input[2]) / (int(_input[2]) - int(_input[0])))
    if (res < 2 and res > -2):
        print(res, "pagina")
    else:
        print(res, "paginas")

    _input = input()