import requests
from bs4 import BeautifulSoup

#%%

def main():
    
    resp = requests.get('https://www.dotblogs.com.tw/YiruAtStudio');
    print(resp.status_code);
    
    soup = BeautifulSoup(resp.text,'html.parser');
    
    main_title = soup.find_all('h3','article__title');
    # print(main_title);
    # print("================================================");
    
    B2 = soup.find_all('h3',{'class':'article__title'})
    # print(B2);
    # print("================================================");
    
    B3 = soup.find_all('h3',class_='article__title')
    # print(B3);
    # print("================================================");

    for title in B3:
        print(title.text);
        print("================================================");
    
    

















#%%

if __name__ == "__main__":
    main();

