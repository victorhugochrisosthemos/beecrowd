x = int(input(''))

exit = 0
answer = 1

while True:
    z = int(input(''))
    if z > x:
        acumulator = x
        for i in range(x+1,z+1):
            answer += 1
            acumulator += i
            if acumulator > z:
                break
        break

print(answer)