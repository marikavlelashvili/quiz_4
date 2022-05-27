import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

f = open('smartphones.csv', 'w',encoding='utf8', newline='\n')
f_obj = csv.writer(f)
h = {'Accept-Language': 'en-US'}
ind = 1
while ind < 11:
    url = 'https://www.ebay.com/b/Apple/bn_21819543?_pgn=' + str(ind)
    r = requests.get(url, headers=h)
    soup_all = BeautifulSoup(r.text, 'html.parser')
    soup = soup_all.find('ul', class_='b-list__items_nofooter srp-results srp-grid')
    all_movies = soup.findAll('li', class_='s-item s-item--large')
    for each in all_movies:
        image = each.find('div', class_='s-item__image-helper')
        url = image.img.get('src')
        title = each.find('h3', class_='s-item__title').text
        price = each.find('span', class_='s-item__price').text
        print(price)
        f_obj.writerow([url, title, price])
    ind += 1
    sleep(randint(15, 20))

f.close()
