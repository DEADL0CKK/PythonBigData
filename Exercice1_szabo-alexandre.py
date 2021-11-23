#Exercice 1

#Question 1
dict = {
    "Sabre Laser":229,
    "Mitendo DX":127.30,
    "Coussin Linux":74.50,
    "Slip Goldorak":29.90,
    "Station Nextpresso":184.60
}

#Question 2
def disponibilite(prod, prix):
    bool = False
    for key,value in dict.items():
        if(prod == key and str(prix) == str(value)):
            bool = True
    return bool


print(disponibilite("Slip Goldorak",29.90))
print(disponibilite("Slip Goldorak",28.90))

#Question 3
def prix_moyen(dict):
    cpt = 0
    result = 0
    for value in dict.values():
        result += value
        cpt += 1
    result = result / cpt
    return result

print(prix_moyen(dict))

#Question 4
def fourchette_prix(prix_min, prix_max, dict):
    list = []
    for key, value in dict.items():
        if prix_min < value and prix_max > value:
            list.append(key)
    return list

print(fourchette_prix(50, 200, dict))

#Question 5
panier = {
    "Sabre Laser":3,
    "Coussin Linux":2,
    "Slip Goldorak":1
}

#Question 6
def tous_disponibles(panier, dict):
    bool = False
    for key in panier.keys():
        if(key in dict.keys()):
            bool = True
        else:
            bool = False
    return bool

print("Disponibilité : ")
print(tous_disponibles(panier, dict)) 

#Question 7
def prix_achats(panier, dict):
    prix_total = 0
    for key,value in panier.items():
        prix_total += (dict[key] * value)
    return prix_total

print("Total : ")
print(prix_achats(panier,dict))