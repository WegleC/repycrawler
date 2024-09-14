import requests
from bs4 import BeautifulSoup

#%%

def main():
    
    resp = requests.get('https://blog.castman.net/py-scraping-analysis-book/ch2/blog/blog.html');
    print(resp.status_code);
    
    soup = BeautifulSoup(resp.text,'html.parser');
    
    main_title = soup.find('a',{"data-foo":"mac-foo"});
    print(main_title);
    print("====================================");
    print(main_title.text);
















#%%

if __name__ == "__main__":
    main();

