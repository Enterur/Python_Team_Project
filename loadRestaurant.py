# saveList.txt에 기록된 음식점 목록을 불러오는 모듈

def load_restaurant():
    inStr = ""
    save_list = []
    inFp = open("C:\\Users\\kimmi\\OneDrive\\바탕 화면\\Python_Team_Project\\saveList.txt", "r", encoding = "UTF-8")

    while True:
        inStr = inFp.readline()
        if inStr == "":
            break
        save_list.append(inStr)

    if not save_list:
        print('\033[31m저장된 음식점이 없습니다. 다시 눌러주세요.\033[0m\n')
        return

    print("저장된 음식점: ")
    for i in save_list:
        print(f'\033[93m\033[1m{i}\033[0m')