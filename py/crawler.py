import requests
from bs4 import BeautifulSoup

#%%

def main():
    
    print("Hello world!");
    url = 'https://www.yannick.com.tw/'
    text = get_tag_text(url,'h3');
    print(text);

#%%



def get_tag_text(url,tag):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text,'html.parser');
        return soup.find(tag).text
    except Exception as e:
        print('Error: %s' % e);
        return None;

#%%

if __name__ == "__main__":
    main();