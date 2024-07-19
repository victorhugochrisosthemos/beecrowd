exit = 0
total = 0
counter = 0

while exit == 0:
    value = input('')
    value = float(value)
    if (value < 0) or (value > 10):
        print('nota invalida')
    else:
        if counter < 2:
            counter += 1
            total += value
        if counter == 2:
            average = total / 2
            average = "{:.2f}".format(average)
            print('media = ' + average)
            option = 0
            while (option < 1 or option > 2):
                print('novo calculo (1-sim 2-nao)')
                option = input('')
                option = float(option)
                if option == 1:
                    break
                if option == 2:
                    exit = 1
            total = 0
            counter = 0