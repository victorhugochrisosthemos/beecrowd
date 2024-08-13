
iterations = int(input())
vector = []
if 1 < iterations < 1000:
    vector = list(map(int, input().split()))
    smaller = min(vector)
    position = vector.index(smaller)
    print(f"Menor valor: {smaller}")
    print(f"Posicao: {position}")



'''
iterations = int(input(''))
vector = []

if (1 < iterations < 1000):
    vector = input('').split(' ')
    vector = [int(number) for number in vector]

    smaller = vector[0]
    position = 0
    for i in range(iterations):
        print(vector[i])
        if vector[i] < smaller:
            smaller = vector[i]
            position = i

print('Menor valor: ' + str(smaller))
print('Posicao: ' + str(position))
'''