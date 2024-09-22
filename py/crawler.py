import requests
import json
#%%

def main():
    r = requests.get('https://stats.moe.gov.tw/files/school/113/school08_new.json')
    
    text = r.content.decode('utf-8-sig')

    data = json.loads(text)
    print(data)

    for school in data:
        print("學年度:",school['學年度'])
        print("學校級別:",school['學校級別'])
        print("學校代碼:",school['學校代碼'])
        print("學校名稱",school['學校名稱'])
        print("郵遞區號",school['郵遞區號'])
        print("地址",school['地址'])

        print("===============================")



    
    
    

#%%

if __name__ == "__main__":
    main();