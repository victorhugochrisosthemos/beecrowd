total_tests = input('')

mouse = 0
frog = 0
rabbit = 0

for i in range(int(total_tests)):
    experiment = input('')
    #print("Animal = " + experiment[-1:])
    number_animals = ''
    for j in range(len(experiment)):
        if(experiment[j] != ' '):
            number_animals += experiment[j]
        else:
            break
    number_animals = int(number_animals)
    #print(number_animals)
    if(experiment[-1:] == 'C'):
        rabbit += number_animals
    elif(experiment[-1:] == 'S'):
        frog += number_animals
    elif(experiment[-1:] == 'R'):
        mouse += number_animals

general_total = rabbit + frog + mouse
rabbit_percent = (rabbit/general_total)*100
frog_percent = (frog/general_total)*100
mouse_percent = (mouse/general_total)*100

general_total = str(general_total)
rabbit = str(rabbit)
frog = str(frog)
mouse = str(mouse)

rabbit_percent = "{:.2f}".format(rabbit_percent)
frog_percent = "{:.2f}".format(frog_percent)
mouse_percent = "{:.2f}".format(mouse_percent)

print("Total: " + general_total + " cobaias")
print("Total de coelhos: " + rabbit)
print("Total de ratos: " + mouse)
print("Total de sapos: " + frog)
print("Percentual de coelhos: " + rabbit_percent + " %")
print("Percentual de ratos: " + mouse_percent + " %")
print("Percentual de sapos: " + frog_percent + " %")