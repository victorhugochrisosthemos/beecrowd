entrada = input()
entrada = entrada.split(" ")
a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])
if a > b:
    if a > c:
        maior = a
    else:
        maior = c
else:
    if b > c:
        maior = b
    else:
        maior = c
print(str(maior) + " eh o maior")