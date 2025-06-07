#리스트에 저장하는 모듈

def save(Input):
    outFp = None
    inFp = ""
    save_list = []

    outFp = open("C:\\Users\\kimmi\\OneDrive\\바탕 화면\\Python_Team_Project\\saveList.txt", "a", encoding="UTF-8")
    inFp = open("C:\\Users\\kimmi\\OneDrive\\바탕 화면\\Python_Team_Project\\saveList.txt", "r", encoding="UTF-8")

    while True:
        inStr = inFp.readline()
        if inStr == "":
            break
        save_list.append(inStr)

    name = Input + "\n"

    if name in save_list:
        outFp.writelines(f'{Input}\n')
        print("---\033[92m음식점을 저장했습니다.\033[0m---")
        print()
    else:
        outFp.writelines(f'{Input}\n')
        print("---\033[92m음식점을 저장했습니다.\033[0m---")
        print()
    
    outFp.close()
    return