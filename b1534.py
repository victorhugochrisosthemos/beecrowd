#b1534

while True:
    try:
        order = int(input())
        
        two = order - 1
        for i in range(order):
            for j in range(order):
                if j == two:
                    print("2", end ="")
                    two -= 1
                elif i == j:
                    print("1", end ="")
                else:
                    print("3", end ="")
            if j != order - 1:
                print(" ",end="")
            else:
                print('')
    except:
        break
