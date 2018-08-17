import requests
from lxml import html


def buleczki():
    id_bulek = {'bagietka_czosnkowa': "16531",
                'polbagietka': "16542",
                'bulka_poranna': "16532"}

    bagietka = requests.get("http://www.biedronka.pl/index.php/pl/product,id," + id_bulek['bagietka_czosnkowa']).text
    # polbagietka = requests.get("http://www.biedronka.pl/index.php/pl/product,id," + id_bulek['polbagietka']).text
    # bulka_poranna = requests.get("http://www.biedronka.pl/index.php/pl/product,id," + id_bulek['bulka_poranna']).text

    bagietka_doc = html.fromstring(bagietka)
    bagietka_html_price = bagietka_doc.cssselect("span")[42].text_content()
    bagietka_price = bagietka_html_price[17:28]
    return "Bagietka Czosnkowa: " + bagietka_price
