from bs4 import BeautifulSoup
import urllib.request as request

url = "http://finance.naver.com/marketindex/"
res = request.urlopen(url)

soup = BeautifulSoup(res, "html.parser")

price = soup.select_one("div.head_info > span.value").string
print("usd/krw = ", price)

'''
$ python bs-usd.py 
usd/krw =  1,127.10
'''