import requests

#%%

def main():
    r = requests.get('https://od.moi.gov.tw/api/v1/rest/datastore/301000000A-002072-044')
    print(r.status_code)
    
    data = r.json()
    # print(data)
    
    for key, value in data.items():
        print(key)



#%%

if __name__ == "__main__":
    main();