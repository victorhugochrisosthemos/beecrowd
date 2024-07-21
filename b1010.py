total = 0
for i in range(2):
    item = input()
    item = item.split(" ")
    cod = int(item[0])
    num = int(item[1])
    valor = round(float(item[2]), 2)
    total = total + num*valor
    
print("VALOR A PAGAR: R$ {:.2f}".format(total))