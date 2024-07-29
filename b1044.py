entrada = input().split()
a, b = entrada
a = int(a)
b = int(b)

if a % b == 0 or b % a == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")