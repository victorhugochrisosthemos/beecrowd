iterations = int(input(''))

if 1 <= iterations <= 3000:
    for i in range(iterations):
        pa, pb, ta, tb = input('').split()
        
        pa = int(pa)
        pb = int(pb)
        ta = float(ta)
        tb = float(tb)

        validation = (100 <= pa < 1000000) and (pa < pb <= 1000000) and (0.1 <= ta <= 10) and (0 <= tb < ta <= 10)

        if validation:
            years = 0
            while pa <= pb:
                pa += int(pa * ta / 100)
                pb += int(pb * tb / 100)
                years += 1
                if years > 100:
                    break
            if years > 100:
                print('Mais de 1 seculo.')
            else:
                print(f'{years} anos.')

'''
O codigo acima é o meu e esse de baixo foi o que passou no teste.
Cara, tá igual, mas enfim, esse de baixo passou

n = int(input())
for i in range(n):
    pa, pb, g1, g2 = input().split()
    pa = int(pa)
    pb = int(pb)
    g1 = float(g1)
    g2 = float(g2)
    a = 0
    while (pa <= pb):
        cpa = int((pa * (g1 / 100)))
        cpb = int((pb * (g2 / 100)))
        a += 1
        pa += cpa
        pb += cpb
        if (a > 100):
            break
    if (a > 100):
        print("Mais de 1 seculo.")
    else:
        print("%d anos." % a)


'''