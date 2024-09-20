import requests

#%%

def main():
    r = requests.get('https://vbs.sports.taipei/opendata/sports_tms2.json')
    data = r.json()
    
    # print(data)
    for info in data:
        print("場地所需分區:",info['Area'])
        print("場地名稱:",info['Name'])
        print("英文場地名稱:",info['NameEng'])
        print("運動型態:",info['SportType'])
        print("地址:",info['Address'])
        print("英文地址：",info['AddressEng'])
        print("開放時間:",info['startTime'])
        print("關閉時間:",info['endTime'])
        print("設施科聯絡電話:",info['LocalCallService'])
        print("=======================================")
    
    
    
    

#%%

if __name__ == "__main__":
    main();