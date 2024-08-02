i = 1
j = 7
while i < 10:
    aux = j
    for k in range(1,4):
        print("I={} J={}".format(i,aux))
        aux -= 1
    j += 2
    i += 2