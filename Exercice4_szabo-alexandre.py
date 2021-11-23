from numpy import NaN
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pandas as pd
import time

ua = UserAgent()
ua.random

headers = {"User-Agent": ua.random}

appt = {
    'title': [],
    'prix':[],
    'pieces':[],
    'nb_chambre':[],
    'surface':[],
    'etage':[],
    'ascenseur':[],
    'terrasse':[],
    'balcon':[],
    'garage':[],
    'box':[],
    'meuble':[],
    'adresse':[]
    }

for cpt in range(1,11):
    print(cpt)

    if(cpt > 1):
        url = f"https://www.seloger.com/immobilier/locations/immo-paris-75/bien-appartement/?LISTING-LISTpg={cpt}"
    else :
        url = "https://www.seloger.com/immobilier/locations/immo-paris-75/bien-appartement/"

    html = requests.get(url, headers=headers)
    if(not(html)):
        print(html)
        break
    soup = BeautifulSoup(html.content, 'html.parser')
    print(soup.title)
    break
    cards = soup.find_all('div', attrs={'data-test':'sl.card-container'})



    for info_card in cards:
        card = info_card.find('div', attrs={'data-test':'sl.detail-top'})
        title = card.find('div',attrs={'data-test':'sl.title'}).text
        prix_label = card.find('div',attrs={'data-test':'sl.price-label'}).text
        prix = prix_label.replace(" ","").split('€')[0]
        ul1 = card.find('ul',attrs={'data-test':'sl.tagsLine_0'}).find_all('li')

        if(info_card.find('div', attrs={'data-test':'sl.address'})):
            adresse = info_card.find('div', attrs={'data-test':'sl.address'}).text
        else:
            adresse = ""    

        nb_chambre = NaN
        surface = NaN
        pieces = NaN
        etage = ""
        ascenseur = False
        terrasse = False
        balcon = False
        garage = False
        box = False
        meuble = False

        for ul in ul1:
            if('pièces' in ul.text):
                pieces = ul.text.split()[0].replace(" ","")
            
            if('chambre' in ul.text or 'ch' in ul.text):
                nb_chambre = ul.text.split()[0].replace(" ","")

            if('m²' in ul.text):
                surface = ul.text.split('m')[0].replace(" ","").replace(",",".")

        if(card.find('ul',attrs={'data-test':'sl.tagsLine_1'})):
            ul2 = card.find('ul',attrs={'data-test':'sl.tagsLine_1'}).find_all('li')
            for ul in ul2:
                if('Ascenseur' in ul.text):
                    ascenseur = True
                if('Terrasse' in ul.text):
                    terrasse = True
                if('Balcon' in ul.text):
                    balcon = True
                if('Garage' in ul.text):
                    garage = True
                if('Box' in ul.text):
                    box = True
                if('meublé' in title):
                    meuble = True
                if('Étage' in ul.text):
                    etage = ul.text

        
            
        appt['title'].append(title)
        appt['prix'].append(prix)
        appt['pieces'].append(pieces)
        appt['nb_chambre'].append(nb_chambre)
        appt['surface'].append(surface)
        appt['etage'].append(etage)
        appt['ascenseur'].append(ascenseur)
        appt['terrasse'].append(terrasse)
        appt['balcon'].append(balcon)
        appt['garage'].append(garage)
        appt['box'].append(box)
        appt['meuble'].append(meuble)
        appt['adresse'].append(adresse)

        # time.sleep(2)




dataframe = pd.DataFrame.from_dict({
    'titre': appt["title"],
    'prix':appt["prix"],
    'pieces':appt["pieces"],
    'nb_chambre':appt["nb_chambre"],
    'surface (m²)':appt["surface"],
    'etage':appt["etage"],
    'ascenseur':appt["ascenseur"],
    'terrasse':appt["terrasse"],
    'balcon':appt["balcon"],
    'garage':appt["garage"],
    'box':appt["box"],
    'meuble':appt["meuble"],
    'adresse':appt["adresse"]
})

dataframe['titre'] = dataframe['titre'].astype(str)
dataframe['prix'] = dataframe['prix'].astype(float)
dataframe['pieces'] = dataframe['pieces'].astype(float)
dataframe['nb_chambre'] = dataframe['nb_chambre'].astype(float)
dataframe['surface (m²)'] = dataframe['surface (m²)'].astype(float)
dataframe['etage'] = dataframe['etage'].astype(str)
dataframe['ascenseur'] = dataframe['ascenseur'].astype(bool)
dataframe['terrasse'] = dataframe['terrasse'].astype(bool)
dataframe['balcon'] = dataframe['balcon'].astype(bool)
dataframe['garage'] = dataframe['garage'].astype(bool)
dataframe['box'] = dataframe['box'].astype(bool)
dataframe['meuble'] = dataframe['meuble'].astype(bool)
dataframe['adresse'] = dataframe['adresse'].astype(str)


print(dataframe)
dataframe.to_excel("Exercice4_resultat_szabo-alexandre.xlsx", index=False)



