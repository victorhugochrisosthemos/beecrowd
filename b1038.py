valor = input()
valor = valor.split(" ")
valor[0] = int(valor[0])
if valor[0] == 1:
    item = 4.0
elif valor[0] == 2:
    item = 4.5
elif valor[0] == 3:
    item = 5.0
elif valor[0] == 4:
    item = 2.0
else:
    item = 1.5
print("Total: R$ {:.2f}".format(item * float(valor[1])))