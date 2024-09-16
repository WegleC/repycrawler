import requests
from bs4 import BeautifulSoup
import re

#%%

def main():
    
    resp = requests.get('https://www.dotblogs.com.tw/YiruAtStudio');
    # print(resp.status_code);
    
    soup = BeautifulSoup(resp.text,'html.parser');
    
    titles = soup.find_all(['h1','h2','h3','h4','h5','h6'])
    # print(titles)

    # for title in titles:
    #     print("=====================")
    #     print(title.text.strip())
    
#%%

    soup = BeautifulSoup(resp.text,'html.parser');
    
    titles = soup.find_all(re.compile('h[1-6]'))
    # print(titles)


    for title in titles:
        print("=====================")
        print(title.text.strip())
    






#%%

if __name__ == "__main__":
    main();

