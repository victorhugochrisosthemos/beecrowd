vetor = []
par = 0
impar = 0
pos = 0
neg = 0
for i in range(5):
    vetor.append(int(input()))
for i in range(5):
    if vetor[i] % 2 == 0:
        par += 1
    else:
        impar += 1
    if vetor[i] > 0:
        pos += 1
    elif vetor[i] < 0:
        neg += 1
print("{} valor(es) par(es)".format(par))
print("{} valor(es) impar(es)".format(impar))
print("{} valor(es) positivo(s)".format(pos))
print("{} valor(es) negativo(s)".format(neg))