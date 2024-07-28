entrada = input()
entrada = entrada.split(" ")
n1, n2, n3 = entrada
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3
    
if (n1 < n2 and n1 > n3) or (n1 > n2 and n1 < n3):
    meio = n1
elif (n2 < n1 and n2 > n3) or (n2 > n1 and n2 < n3):
    meio = n2
else:
    meio = n3
    
if n1 != maior and n1 != meio:
    menor = n1
elif n2 != maior and n2 != meio:
    menor = n2
else:
    menor = n3
    
print(str(menor))
print(str(meio))
print(str(maior))
print("")
print(str(n1))
print(str(n2))
print(str(n3))