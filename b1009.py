nome = input()
sal = round(float(input()), 2)
vendas = round(float(input()),2)
print("TOTAL = R$ {:.2f}".format(sal + 0.15*vendas))