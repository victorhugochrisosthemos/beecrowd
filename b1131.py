exit = 0
draw = 0
total_inter = 0
total_gremio = 0
counter = 0

while exit == 0:
    inter,gremio = input('').split(' ')
    counter += 1
    inter = int(inter)
    gremio = int(gremio)
    
    if inter == gremio:
        draw += 1
    else:
        if inter > gremio:
            total_inter += 1
        else:
            total_gremio += 1
    
    option = 0
    while option != 1 or option != 2:
        print('Novo grenal (1-sim 2-nao)')
        option = int(input(''))
        if option == 2:
            exit = 1
            break
        if option == 1:
            break
        
print(str(counter) + ' grenais')
print('Inter:' + str(total_inter))
print('Gremio:' + str(total_gremio))
print('Empates:' + str(draw))

if total_inter > total_gremio:
    print('Inter venceu mais')
elif total_gremio > total_inter:
    print('Gremio venceu mais')
else:        
    print('Nao houve vencedor')