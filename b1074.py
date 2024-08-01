n = int(input())
for i in range(n):
    frase = ''
    a = int(input())
    if a == 0:
        frase += 'NULL'
    else:
        if a % 2 == 0:
            frase += 'EVEN '
        else:
            frase += 'ODD '
        if a > 0:
            frase += 'POSITIVE'
        else:
            frase += 'NEGATIVE'
    print(frase)