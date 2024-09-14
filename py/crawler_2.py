import requests
from bs4 import BeautifulSoup

#%%

def main():
    
    resp = requests.get('https://www.dotblogs.com.tw/YiruAtStudio');
    print(resp.status_code);
    
    soup = BeautifulSoup(resp.text,'html.parser');
    
    print("======1======")
    
    print(soup.find('h3').text);
    
    print("======2======")

    print(soup.h3.text)
    
    print("======3======")
    
    print(soup.h3.a.text)

    print("======4======")

    print(soup.h3.string)
    
    print("======5======")

    print(soup.h3.a.string)



















#%%

if __name__ == "__main__":
    main();

