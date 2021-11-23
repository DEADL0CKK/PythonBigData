from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

wd= webdriver.Chrome('chromedriver',chrome_options=chrome_options)

url = "https://www.seloger.com/immobilier/locations/immo-paris-75/bien-appartement/"
wd.get(url)
print(wd.page_source)
# print(wd.find_element_by_xpath('//html/body/div[3]/div/div[3]/div[2]/div[2]/div[3]/div[3]/div[1]/div[1]/div/div[1]'))
#root > div > div.Page__Slice-st6q56-0.ePzVtF > div.Page__Wrap-st6q56-1.kavOcA > div.Page__WrapMain-st6q56-3.dHrhZe > div:nth-child(1) > div.Card__ContentZone-sc-7insep-2.diTKck > div:nth-child(1)