import requests


#%%

def main():

    r = requests.get('https://tw.rter.info/capi.php')
    data = r.json()
    # print(data)
    
    for currency, info in data.items():
        # print(currency)
        # print(info)
        
        exrate = info['Exrate']
        # print(exrate)
        
        updatetime = info['UTC']
        # print(updatetime)
        
        print(f"Currency:{currency},Exrate:{exrate},Updatetime:{updatetime}")




#%%

if __name__ == "__main__":
    main();

