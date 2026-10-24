def compte_voyelles(texte) :
    nbre_voyelles = 0
    for lettre in texte :
        if lettre.lower() in "aeiouy" :
            nbre_voyelles += 1
    return nbre_voyelles

print(compte_voyelles("Ensimag"))