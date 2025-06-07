# API서버에서 받은 값들을 정리해주는 모듈

def filter_restaurant(places, selected_category):
    filtered_places = []

    for place in places:
        category = place.get("category_name", "N/A")
        if selected_category in category:
            restaurant_dict = {
                "Place Name": place.get("place_name", 'N/A'),
                "Address": place.get("address_name", "N/A"),
                "Distance": place.get("distance", "N/A") + "m",
                "Category": place.get("category_name", "N/A"),
                "Phone": place.get("phone", "N/A")
            }
            filtered_places.append(restaurant_dict)
        
    if not filtered_places:
        print("""\033[31m 입력하신 카테고리가 검색되지 않았습니다. 가까운 순으로 다른 음식점을 추천합니다.\n
        입력하신 반경 내에 음식점이 없을 경우 추천이 되지 않습니다.\033[0m""")
        print()
        for place in places:
            restaurant_dict = {
                "Place Name": place.get("place_name", 'N/A'),
                "Address": place.get("address_name", "N/A"),
                "Distance": place.get("distance", "N/A") + "m",
                "Category": place.get("category_name", "N/A"),
                "Phone": place.get("phone", "N/A"),
                "Kakao Map URL": place.get("place_url", "N/A")
            }
            filtered_places.append(restaurant_dict)

    
    return filtered_places