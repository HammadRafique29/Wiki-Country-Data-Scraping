import requests
from bs4 import BeautifulSoup
from threading import Thread

# hello! this is my first time using python, so bear with me.
# please assist me in any errors you find, i would like to know how to improve my python skills :)


def SAVE(file_name, data):
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(str(data)+"\n")

def scrape_paragraphs(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        paragraphs = soup.find_all('p')
        for paragraph in paragraphs:
            # so what i ended up doing, since i was unable to scrap all of them together (run time took too long)
            # or it would only show me the first three countries and skip the rest
            # because these pages are content heavy, i used a if else statement to scrape only sections that include key words used in the assignment!
            # the logic seems correct, but i know there's a more efficient way to scrape data
            # let me know your thougths!
            if 'GDP' in paragraph.text or 'capital' in paragraph.text or 'language' in paragraph.text or 'area' in paragraph.text or 'population' in paragraph.text:
                SAVE(f"{url.split('/')[-1]}.txt", paragraph.text)  
    else:
        print(f"Unable to find content in {url}. Error code {response.status_code}")
        


urls = [
    'https://en.wikipedia.org/wiki/Canada',
    'https://en.wikipedia.org/wiki/United_States',
    'https://en.wikipedia.org/wiki/United_Kingdom',
    'https://en.wikipedia.org/wiki/Korea',
    'https://en.wikipedia.org/wiki/France',
    'https://en.wikipedia.org/wiki/Turkey',
    'https://en.wikipedia.org/wiki/Italy'
# one thing is that korea combines both north and south korea here. i was tempted to just use just south korea's information
]


for url in urls:
    t1 = Thread(target=scrape_paragraphs, args=[url])
    t1.start()
