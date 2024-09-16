import requests
from bs4 import BeautifulSoup

#%%

def main():
    
    resp = requests.get('https://blog.castman.net/py-scraping-analysis-book/ch2/blog/blog.html');
    # print(resp.status_code);
    
    soup = BeautifulSoup(resp.text,'html.parser');
    
    divs = soup.find_all('div','content');
    # print(divs)
    
    for div in divs:
        print("=============")
        print(div.h6.text.strip())
        print(div.a.text.strip())
        print(div.p.text.strip())













#%%

if __name__ == "__main__":
    main();

