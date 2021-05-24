from bs4 import BeautifulSoup
import urllib.request as request

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

res = request.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

title = soup.find("title").string
wf = soup.find("wf").string
print(title)
print(wf)

'''
$ python bs-weather_rss.py
기상청 육상 중기예보
○ (강수) 27일(목)은 수도권과 강원영서, 전남권, 경남권, 제주도에 비가 오겠습니다. 한편, 28일(금) 오후에는 수도권과 강원영서에 비가 오겠 
습니다. <br />○ (기온) 이번 예보기간의 아침 기온은 12~18도, 낮 기온은 19~29도로 어제(23일, 아침최저기온 12~21도, 낮최고기온 22~31도)보 
다 낮겠습니다.<br />○ (주말전망) 29일(토)과 30일(일)은 맑겠습니다. 아침 기온은 12~16도, 낮 기온은 21~28도가 되겠습니다.
'''