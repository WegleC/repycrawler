import requests
from bs4 import BeautifulSoup

#%%

def main():
    
    resp = requests.get('https://www.dotblogs.com.tw/YiruAtStudio');
    print(resp.status_code);
    
    soup = BeautifulSoup(resp.text,'html.parser');
    
    main_title = soup.find_all('h3');
    # print(main_title);
    
    for title in main_title:
        print(title.text);
        print("====================================================")


















#%%

if __name__ == "__main__":
    main();

