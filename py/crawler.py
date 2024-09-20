import requests

#%%

r = requests.get('https://raw.githubusercontent.com/wsmwason/taiwan-bank-code/master/data/taiwanBankCodeATM.json')
data = r.json()

# print(data)
for bank_info in data:
    print("BankCode:",bank_info['code'])
    print("Bank:",bank_info['name'])