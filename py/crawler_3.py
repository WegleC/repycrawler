import requests
from bs4 import BeautifulSoup

#%%

def main():
    r = requests.get('https://member.lccnet.com.tw/Courses/5020240813213034')
    # print(r.status_code)
    
    soup = BeautifulSoup(r.text,'html.parser')
    print(soup)
    


#%%

if __name__ == "__main__":
    main();