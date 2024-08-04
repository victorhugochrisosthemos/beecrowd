def fat(n):
    valor = 1
    for i in range(1,n+1):
        valor *= i
    return valor
try:
    while True:
        entrada = input()
        if not entrada:
            break
        n1, n2 = map(int, entrada.split())
        resposta = fat(n1) + fat(n2)
        print(resposta)
except EOFError:
    pass