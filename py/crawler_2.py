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
        all_tds = row.find_all('td')
        # print(all_tds)
        if 'href' in all_tds[3].a.attrs:
            href = all_tds[3].a['href']
        else:
            href = None
        
        print(all_tds[0].text,"||",all_tds[1].text,"||",all_tds[2].text,"||",href,"||",all_tds[3].a.img['src'],"||")

#%%

if __name__ == "__main__":
    main();

