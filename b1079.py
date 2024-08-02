n = int(input())
vetor = []
for i in range(1, n+1):
    n1,n2,n3=map(float,input().split())
    r=(n1*2+n2*3+n3*5)/10
    vetor.append(round(r,1))
for i in range(0, n):
    print(str(vetor[i]))