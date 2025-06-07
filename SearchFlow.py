from kakaoAPI import api
from filter import filter_restaurant
from dataFrame import restaurant_DataFrame
from randomChoice import random_choice

def search_flow(x, y, radius):
    random_list = []

    selected_category = input("원하는 음식점 종류 (예: 한식 중식 일식): ")
    places = api(x, y, radius)

    if not selected_category:
        filtered_list = filter_restaurant(places, "N/A")
        restaurant_DataFrame(filtered_list)
        random_list.append(filtered_list)
    else:
        selected = selected_category.split()
        
        for i in selected:
            filtered_list = filter_restaurant(places, i)
            message = f'\033[35m\033[1m{i}\033[0m'
            print('{0:=^150}'.format(message))
            restaurant_DataFrame(filtered_list)
            random_list.append(filtered_list)
            print()

    a = random_list[0]
    if not a:
        print(f'{"":=^30}')
        print()
    else:
        random_choice(random_list)