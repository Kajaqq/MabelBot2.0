import requests
from lxml import html


def gitgud(text_input):
    gitgud_get = requests.get("https://github.com/search?q=" + text_input.replace(' ', '+')).text
    gitgud_doc = html.fromstring(gitgud_get)
    gitgud_description = gitgud_doc.cssselect("p")[6].text_content()[18:][:-7]
    gitgud_fulltitle = gitgud_doc.cssselect("a")[40].text_content()
    gitgud_stars = gitgud_doc.cssselect("a.muted-link")[1].text_content().replace(' ', '').replace('\n', '')
    gitgud_link = "https://github.com/" + gitgud_fulltitle

    # print(gitgud_fulltitle)
    # print(gitgud_description)
    # print(gitgud_link)
    # print(gitgud_stars)

    return "Znalazlem to:\n" + gitgud_fulltitle + "\nOpis: " + gitgud_description + "\nGwiazdki: " + gitgud_stars + "\n\n" + gitgud_link
    
