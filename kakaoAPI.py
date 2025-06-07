# API서버에 원하는 정보를 요청하고 그 값을 받는 모듈

import requests

def api(x, y, radius):
    url = "https://dapi.kakao.com/v2/local/search/category.json"
    search_info = {
        "category_group_code": "FD6",
        "x": str(x), 
        "y": str(y),
        "radius": radius,
        "sort": "distance"
    }

    headers = {
        "Authorization": "KakaoAK 1a251a6ce8afd58ca6fd538cfefab12b"
    }

    res = requests.get(url, params=search_info, headers=headers)

    if res.status_code == 200:
        return res.json()["documents"]
    
    else:
        print("API 요청 실패:", res.status_code)
        print("응답 내용:", res.text)