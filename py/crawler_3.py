import requests

#%%
# 各縣市初婚年齡
def main():
    r = requests.get('https://od.moi.gov.tw/api/v1/rest/datastore/301000000A-002072-044')
    print(r.status_code)
    
    data = r.json()
    # print(data['result']['records'])
    records = data['result']['records']
    # print(records)
    # print(len(records))
    records_len = len(records)
    
    for i in range(records_len):
        print("==============================")
        for key, value in records[i].items():
            print(key+":", value)




#%%

if __name__ == "__main__":
    main();