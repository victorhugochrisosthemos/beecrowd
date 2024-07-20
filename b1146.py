exit = 0

while exit == 0:
    value = int(input(''))
    if(value != 0):
        for i in range(value):
            sum = i + 1
            print(str(sum),end="")
            if value != (i+1):
                print(' ',end="")
            else:
                print('')
    else:
        exit = 1