import requests
from bs4 import BeautifulSoup

url = "https://fr.wikipedia.org/wiki/Naissances_en_France_suivant_la_nationalit%C3%A9_de_la_m%C3%A8re"
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')

tables = soup.find_all('table', attrs={'class':'wikitable'})
list = []

for table in tables:

    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    title = rows[1].find_all('th')
    dict = {}
    if(len(title)>2):
        for row in rows:
            cols = row.find_all('td')
            if(len(cols)>0):
                dict[cols[0].text]= {title[0].text:cols[1].text,
                            title[1].text:cols[2].text,
                            title[2].text:cols[3].text
                }
    list.append(dict)



print(list)