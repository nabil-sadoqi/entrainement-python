def valeur_finale(capital, taux, annees) :
    for _ in range(annees) :
        capital = capital + capital*taux
    return capital

print(round(valeur_finale(1000, 0.05, 10), 2))   # 1628.89
capital = 1000
taux = 0.05
annees = 10
print(round(capital * (1 + taux) ** annees, 2))