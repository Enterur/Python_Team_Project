# 메인 프로그램

from SearchFlow import search_flow
from loadRestaurant import load_restaurant

def main():
    print("==== 상명대 정문 위도 / 경도: 37.6025 / 126.9553 ====\n")

    while True:
        print("1. 음식점 검색 및 추천")
        print("2. 저장된 음식점 목록 보기")
        print("3. 종료")
        choice = input("원하는 작업을 선택하세요 (1/2/3): ")
        print()

        if choice == '1':
            y = 37.6025
            x = 126.9553
            while True:
                try:
                    radius = int(input("반경(m): "))
                    break
                except ValueError:
                    print('\033[31m\033[1m다시 입력해주세요.\n\033[0m')
            
            search_flow(x, y, radius)
        elif choice == '2':
            load_restaurant()
        elif choice == '3':
            print('\033[34m\033[1m프로그램을 종료합니다. 감사합니다!\033[0m')
            break
        else:
            print('\033[31m\033[1m잘못된 입력입니다. 다시 시도해주세요.\n\033[0m')

if __name__ == "__main__":
    main()