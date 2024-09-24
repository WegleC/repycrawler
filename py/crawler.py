import requests
import json
#%%

def main():
    r = requests.get('https://www.twnic.tw/dnjson.json')
    
    text = r.content.decode('utf-8-sig')

    data = json.loads(text)
    # print(data)

    for net in data:
        print("網域名稱:",net['網域名稱'])
        print("統計年月:",net['統計年月'])
        print("數量:",net['數量'])
    
        print("===================================")



    
    
    

#%%

if __name__ == "__main__":
    main();