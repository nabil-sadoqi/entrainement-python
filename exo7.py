def inverse(texte) :
    inv_texte = ""
    for lettre in texte :
        inv_texte = lettre + inv_texte
    return inv_texte

def est_palindrome(texte) :
    min_texte = texte.lower()
    return inverse(min_texte) == min_texte

print(est_palindrome("Radar"))    # True
print(est_palindrome("Python"))   # False