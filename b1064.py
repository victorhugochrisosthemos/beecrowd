n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())
n = 0
soma = 0
if n1 > 0:
    n += 1
    soma += n1
if n2 > 0:
    n += 1
    soma += n2
if n3 > 0:
    n += 1
    soma += n3
if n4 > 0:
    n += 1
    soma += n4
if n5 > 0:
    n += 1
    soma += n5
if n6 > 0:
    n += 1
    soma += n6
print("{} valores positivos".format(n))
print('{:.1f}'.format(soma/n))