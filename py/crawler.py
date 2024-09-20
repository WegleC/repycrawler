

#%%

def main():
    my_dict = {
        'a' : '46',
        'b' : '50',
        'c' : '98',
        'd' : '83',
        'e' : '76',
    }
    
    for key_1 in my_dict.keys():
        print(key_1)
        
    for value_1 in my_dict.values():
        print(value_1)
    
    for key,value in my_dict.items():
        print(key)
        print(value)
        print("===============")


#%%

if __name__ == "__main__":
    main();