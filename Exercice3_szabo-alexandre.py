#Exercice 3
def est_lettre(c):
    """ str -> bool
    Hypothèse : len(c) == 1 (caractère)
    Retourne True si le caractère c est une lettre, ou False sinon."""
    return ((c >= 'a') and (c <= 'z')) \
    or ((c >= 'A') and (c <= 'Z')) \
    or (c in {'é', 'è', 'à', 'ù', 'oe'})

def chargement_texte(fichier):
    """ str -> str
    Hypothèse : le fichier est présent sur le disque
    Retourne la chaîne de caractères correspondant au contenu
    du fichier."""
    # contenu : str
    contenu = '' # contenu du fichier
    with open(fichier, 'r') as f:
        contenu = f.read()
    return contenu

#Question 1
def frequences_lettres(chaine):
    word = list(chaine)
    dict = {}
    for i in word:
        if(est_lettre(i)):
            if(i in dict):
                dict[i] += 1
            else:
                dict[i] = 1
    return dict

print(frequences_lettres("l'élève"))

#Question 2
def lettre_freq_max(text):
    max_value = 0
    for key,value in text.items():
        if(value > max_value):
            max_value = value
            max_key = key
    return max_key

print(lettre_freq_max(frequences_lettres("l'élève")))

#Question 3
texte = chargement_texte("texte.txt")
print(frequences_lettres(texte))
print(lettre_freq_max(frequences_lettres(texte)))

#Question 4
def lettres_freq_inf(dict, seuil):
    list = []
    for key,value in dict.items():
        if(value <= seuil):
            list.append(key)
    return list

print(lettres_freq_inf(frequences_lettres("l'élève"),2))

#Question 5
print(lettres_freq_inf(frequences_lettres(texte),100))