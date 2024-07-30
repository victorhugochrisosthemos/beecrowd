n = float(input())
if n >= 0 and n <= 400:
    sal = n*1.15
    per = 15
elif n > 400 and n <= 800:
    sal = n*1.12
    per = 12
elif n > 800 and n <= 1200:
    sal = n*1.1
    per = 10
elif n > 1200 and n <= 2000:
    sal = n*1.07
    per = 7
elif n > 2000:
    sal = n*1.04
    per = 4
print("Novo salario: {:.2f}".format(sal))
print("Reajuste ganho: {:.2f}".format(sal - n))
print("Em percentual: {} %".format(per))