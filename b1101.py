while True:
    values = input()
    first = ''
    second = ''
    sum = 0
    
    # Processa a entrada para separar os dois números
    for i in range(len(values)):
        if values[i] == ' ':
            for j in range(i):
                first = first + values[j]
            for k in range(i + 1, len(values)):
                second = second + values[k]
                
    first = int(first)
    second = int(second)

    # Condição de saída
    if first <= 0 or second <= 0:
        break

    # Garante que first seja menor ou igual a second
    if first > second:
        first, second = second, first

    # Calcula a soma e gera a saída
    for p in range(first, second + 1):
        print('%d ' % p, end="")
        sum += p
    print('Sum=%d' % sum)

    