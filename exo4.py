def maximum(liste) :
    if len(liste) == 0:
        return 'liste vide'
    max = liste[0]
    for nombre in liste :
        if nombre > max :
            max = nombre
    return max

print(maximum([3, 17, 5, 9]))   # 17
print(maximum([-4, -2, -8]))    # -2
print(maximum([]))