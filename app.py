from selenium import webdriver
from bs4 import BeautifulSoup

import database

for n in range(1,40):
    url_to_scrap = 'https://www.animefenix.com/animes?page={0}'.format(n)

    driver = webdriver.Firefox(executable_path='geckodriver')
    driver.get(url_to_scrap)

    html_code = driver.page_source

    soup = BeautifulSoup(html_code,'lxml')

    all_url = soup.findAll('figure',class_="image")

    for url in all_url:
        title = url.find('img')['alt'].replace("'"," ")
        poster = url.find('img')['src']
        anime_url = url.find('a')['href']

        data = {
            "title" : title,
            "poster" : poster,
            "url" : anime_url
        }
        
        database.addAnime(data)
    
    driver.close()

print('SUCCESSFUL')