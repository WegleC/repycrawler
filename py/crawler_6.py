import requests
import json
#%%
#大專校院名錄
def main():
    r = requests.get('https://stats.moe.gov.tw/files/school/113/u1_new.json');
    
    text = r.content.decode('utf-8-sig');
    
    data = json.loads(text);
    
    # print(data);
    
    for school in data:
        print("學校名稱:",school['學校名稱'])
        print("地址:",school['地址'])
        print("電話:",school['電話'])
        print("網址:",school['網址'])
        print("=========================================")


















#%%
if __name__ == "__main__":
    main();