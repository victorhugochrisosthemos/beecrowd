n1 = input()
n2 = input()
n3 = input()
if n1 == 'vertebrado':
    if n2 == 'ave':
        if n3 == 'carnivoro':
            valor = 'aguia'
        else:
            #onivoro
            valor = 'pomba'
    else:
        #mamifero
        if n3 == 'onivoro':
            valor = 'homem'
        else:
            #herbivoro
            valor = 'vaca'
else:
    #invertebrado
    if n2 == 'inseto':
        if n3 == 'hematofago':
            valor = 'pulga'
        else:
            #herbivoro
            valor = 'lagarta'
    else:
        #anelideo
        if n3 == 'hematofago':
            valor = 'sanguessuga'
        else:
            #onivoro
            valor = 'minhoca'
print(valor)