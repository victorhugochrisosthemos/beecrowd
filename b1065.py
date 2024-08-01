vetor = []
soma = 0
for i in range(0,5):
    vetor.append(int(input()))
    if vetor[i]%2==0:
        soma += 1
print("{} valores pares".format(soma))