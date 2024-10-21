
from crawler_2 import main as crawler_2
from crawler_4 import main as crawler_4
from crawler_5 import main as crawler_5
from crawler_6 import main as crawler_6
from crawler_7 import main as crawler_7
from crawler_8 import main as crawler_8

def menu_print():
    print("-----台灣各級學校統計資料查詢系統-----")
    print("0：離開系統")
    print("1：幼兒園名錄")
    print("2：國民小學名錄")
    print("3：國民中學名錄")
    print("4：高級中等學校名錄")
    print("5：大專校院名錄")
    print("6：軍警大專校院名錄")
    print("--------------------------------")

def execute_crawler(option):
    crawlers = {
        "1": crawler_8,
        "2": crawler_2,
        "3": crawler_5,
        "4": crawler_4,
        "5": crawler_6,
        "6": crawler_7
    }
    if option in crawlers:
        print("\n")
        crawlers[option]()
        print("\n")
        return True
    return False

def main():
    n = 0
    while True:
        menu_print()
        menu_use = input("請輸入想要查詢的資料代碼：")
        if menu_use == "0":
            print("\n")
            print("感謝您的使用，稍後將離開系統")
            print("\n")
            break
        elif execute_crawler(menu_use):
            continue
        else:
            n += 1
            print("\n")
            if n < 3:
                print("無此資料代碼，請重新輸入")
                print("\n")
            else:
                print("輸入錯誤次數已超過上限，系統將自動退出")
                print("\n")
                break

if __name__ == "__main__":
    main()