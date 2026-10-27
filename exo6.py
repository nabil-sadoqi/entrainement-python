def inverse(texte) :
    inv_texte = ""
    for lettre in texte :
        inv_texte = lettre + inv_texte
    return inv_texte

print(inverse("python"))   # nohtyp