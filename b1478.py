while True:
    value = int(input())
    if value == 0:
        break

    matrix = []
    
    for i in range(value):
        line = []
        for j in range(value):
            show = abs(i - j) + 1
            line.append(show)
        matrix.append(line)
    
    for cel in matrix:
        text = ' '.join(f"{num:>3}" for num in cel)
        print(text)
    print("")