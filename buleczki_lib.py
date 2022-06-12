import re
import requests
from bs4 import BeautifulSoup
'''
    A library for scrapping Biedronka prices for bread rolls.
'''
def buleczki():
    URL= "http://www.biedronka.pl/index.php/pl/product,id,"
    id_bulek = {'Bagietka Czosnkowa': "16531",
                u'Półbagietka': "16542",
                u'Bułka Poranna': "16532"}
    
    for buleczka in id_bulek:
            id = id_bulek[buleczka]  
            bagietka = requests.get(URL+id).text
            bagietka_soup = BeautifulSoup(bagietka, 'html.parser')
            bagietka_html_span = bagietka_soup.select_one("span[class*=product]").text
            bagietka_price_per_kg = re.findall(r'[-+]?(\d+([.,]\d*)?|[.,]\d+)([eE][-+]?\d+)?', bagietka_html_span)[0][0] # price per kg viaq regex
            bagietka_weight = bagietka_soup.select_one("h3[style*=margin]").text
            bagietka_weight = re.findall(r'\b\d+\b', bagietka_weight) #weight in grams, via regex
            bagietka_price_per_gram = float(bagietka_price_per_kg.replace(',', '.'))/1000
            bagietka_price = int(bagietka_weight[0]) * float(bagietka_price_per_gram)
            bagietka_price_str = (f'{round(bagietka_price, 2)}zł')
            print (f'{buleczka}: {bagietka_price_str}')


if __name__ == '__main__':
    buleczki()