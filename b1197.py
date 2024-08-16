try:
    while True:
        entrada = input()
        if not entrada:
            break

        v, t = map(int, entrada.split())
        deslocamento = v * t * 2
        print(deslocamento)

except EOFError:
    pass