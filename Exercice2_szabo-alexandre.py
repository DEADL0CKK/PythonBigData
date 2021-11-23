#Exercice 2
Dessert = {
    'gateau chocolat' : {'chocolat', 'oeuf', 'farine', 'sucre', 'beurre'},
    'gateau yaourt' : {'yaourt', 'oeuf', 'farine', 'sucre'},
    'crepes' : {'oeuf', 'farine', 'lait'},
    'quatre-quarts' : {'oeuf', 'farine', 'beurre', 'sucre'},
    'kouign amann' : {'farine', 'beurre', 'sucre'}
}

#Question 1
def nb_ingredients(dessert, recette):
    return len(dessert[recette])

print(nb_ingredients(Dessert,'gateau chocolat'))

#Question 2
def recette_avec(dessert, ingredient):
    list = []
    for key,value in dessert.items():
        if(ingredient in value):
            list.append(key)
    return list

print(recette_avec(Dessert,'lait'))

#Question 3
def tous_ingredients(dessert):
    list = []
    for value in dessert.values():
        for i in value:
            if(i not in list):
                list.append(i)
    return list

print(tous_ingredients(Dessert))

#Question 4
def table_ingredients(dessert):
    dict = {}
    for key,value in dessert.items():
        for i in value:
            if(i in dict):
                dict[i].append(key)
            else:
                dict[i] = [key]
    return dict

print(table_ingredients(Dessert))

#Question 5
def ingredient_principal(dessert):
    dict = {}
    for key,value in dessert.items():
        for i in value:
            if( i in dict):
                dict[i] +=1
            else:
                dict[i] = 1
    return max(dict, key=dict.get)

print(ingredient_principal(Dessert))

#Question 6
def recette_sans(dessert, ingredient):
    dict = {}
    for key, value in dessert.items():
        if(ingredient not in value):
            dict[key] = value
    return dict

print(recette_sans(Dessert,'oeuf'))