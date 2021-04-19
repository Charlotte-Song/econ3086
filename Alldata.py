# collect the latest price of each shoes

import urllib.request
import bs4
import ssl
import pandas as pd


# read html based on url
def get_html(url):
    ssl._create_default_https_context = ssl._create_unverified_context
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
    url = 'https://stockx.com/sneakers'
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)
    text = response.read().decode()
    html = bs4.BeautifulSoup(text, 'html.parser')
    return html


# 还没有想好怎么写完能够自动读取到页数
def get_page_num():
    html = get_html('https://stockx.com/sneakers')
    page_container = html.find("div", attrs={"class", "css-zfbjl9-PaginationContainer"})
    pages = html.find_all("ul", attrs={"class", "css-tcf6ot-ButtonList"})


# format the list of url based on the number of page
urls = ['https://stockx.com/sneakers?page={}'.format(i)
        for i in range(1, 26)]
# for each page read the name of the shoes
for url in urls:
    ssl._create_default_https_context = ssl._create_unverified_context
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)
    text = response.read().decode()
    html = bs4.BeautifulSoup(text, 'html.parser')
    shoes = html.find_all("div", attrs={"class", "tile browse-tile"})
    for shoe in shoes:
        name = shoe.find('a').get('href')
        print(name)

