import requests
from bs4 import BeautifulSoup
import re

#%%

def main():
    
    resp = requests.get('http://blog.castman.net/py-scraping-analysis-book/ch2/table/table.html');
    print(resp.status_code);
    
    soup = BeautifulSoup(resp.text,'html.parser');
    
    prices = []
    
    row_a = soup.find('table','table')
    # print(row_a)
    
    row_b = row_a.tbody.find_all('tr')
    # print(row_b)
    
    for row in row_b:
        pp = row.find_all('td')[2].text
        prices.append(int(pp))

    print(prices)
    print(sum(prices))
    print(len(prices))


#%%

if __name__ == "__main__":
    main();

