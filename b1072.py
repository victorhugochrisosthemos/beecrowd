n = int(input())
vetor = []
for i in range(n):
    vetor.append(int(input()));
dentro = 0
fora = 0
for i in range(n):
    if 10 <= vetor[i] <= 20:
        dentro += 1
    else:
        fora += 1
print("{} in".format(dentro))
print("{} out".format(fora))