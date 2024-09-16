import requests
from bs4 import BeautifulSoup
import re

#%%

def main():
    
    resp = requests.get('https://live.rookiesavior.net/');
    # print(resp.status_code);
    
    soup = BeautifulSoup(resp.text,'html.parser');
    
    imgs = soup.find_all('img')
    # print(imgs)

    # for img in imgs:
    #     if 'src' in img.attrs:
    #         if img['src'].endswith('.png'):
    #             print(img['src'])

#%%

    for img in soup.find_all('img',{'src':re.compile('.png')}):
        print(img['src'])



#%%

if __name__ == "__main__":
    main();

