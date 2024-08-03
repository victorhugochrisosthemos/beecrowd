i = 0
j1 = 1
j2 = 2
j3 = 3
while i <= 2:
    print("I={} J={}".format(i,j1))
    print("I={} J={}".format(i,j2))
    print("I={} J={}".format(i,j3))
    j1 += 0.2
    j2 += 0.2
    j3 += 0.2
    i += 0.2
    if not j1.is_integer():
        j1 = round(j1,1)
        j2 = round(j2,1)
        j3 = round(j3,1)
    else:
        j1 = int(j1)
        j2 = int(j2)
        j3 = int(j3)
    if not i.is_integer():
        i = round(i,1)
    else:
        i = int(i)