import requests
from bs4 import BeautifulSoup

#%%

reqs= requests.get('https://blog.castman.net/py-scraping-analysis-book/ch1/connect.html')
# print(reqs)
# print(reqs.text)

soup = BeautifulSoup(reqs.text,'html.parser')
# print(soup)

get_h1 = soup.find('h1').text

print(get_h1)


get_p = soup.find('p').text

print(get_p)


get_a = soup.find('a').text

print(get_a)


get_footer = soup.find('footer').text

print(get_footer)