from itertools import combinations

n = int(input())
if (n >= 1 and n <= 100000):
    
    teste = [int(input()) for _ in range(n)]

    
    #teste = [60, 30, 20, 40, 60]
    
    original = teste[:]
    
    #print("Original:")
    #print(original)
    
    # Remove duplicados e ordena para o conjunto dos não consecutivos
    teste = sorted(set(teste))
    
    #print("Únicos:")
    #print(teste)
    
    # Conjunto dos não consecutivos
    max_unicos = 0
    
    # Gera todas as combinações possíveis de 3 elementos distintos
    for a, b, c in combinations(teste, 3):
        if a + b > c and a + c > b and b + c > a:
            max_unicos = max(max_unicos, 3)
    
    # Conjunto dos consecutivos
    max_consecutivos = 0
    atual_consecutivo = 0
    
    for i in range(len(original) - 2):
        a, b, c = original[i], original[i + 1], original[i + 2]
        if a + b > c:
            atual_consecutivo = atual_consecutivo + 1 if max_consecutivos > 0 else 3
            max_consecutivos = max(max_consecutivos, atual_consecutivo)
        else:
            atual_consecutivo = 0
    
    # Ajustar para zero caso não tenha subsequências válidas
    max_consecutivos = max_consecutivos if max_consecutivos >= 3 else 0
    max_unicos = max_unicos if max_unicos >= 3 else 0
    
    #print("Não consecutivos:", max_unicos)
        #print("Consecutivos:", max_consecutivos)
        
    print(max_unicos)
    print(max_consecutivos)
