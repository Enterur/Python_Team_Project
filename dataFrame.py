# 가져온 데이터를 보기 좋게 만들어주는 모듈

import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 150)

def restaurant_DataFrame(filtered_places):
    df = pd.DataFrame(filtered_places)
    print(df)