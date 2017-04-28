import requests
import pprint
# from bs4 import BeautifulSoup

filmInfoPattern = 'http://www.wandafilm.com/trade/time.do?m=init&city_code=6038070126&cinema_id=137&day=%s&rond=541'
print(filmInfoPattern%'2017_04_12')
data = requests.get(filmInfoPattern%'2017_04_12')
pprint.pprint(data.json())
# soup = BeautifulSoup(data.read(), 'html.parser')
# print(soup.prettify())
# print("%s%s"%33)
# 6038070126
# _day = "2017_04_12", _cinema_id = "137", _city_code = "6038070126"