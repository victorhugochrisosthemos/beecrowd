value = int(input(''))

first = 0
second = 0
third = 0

if(value > 1 and value < 1000):
    for i in range(value):
        first = i + 1
        second = first**2
        third = first**3
        print('{} {} {}'.format(first,second,third))

        second += 1
        third += 1

        print('{} {} {}'.format(first,second,third))
        
