
import requests
from bs4 import BeautifulSoup


result = []
url = ("https://technews.tw/2019/11/05/morris-chang-says-college"
       "-education/?fbclid=IwAR3ImlwSDhf3uR-s4EzgmLzuWUltx4Kzl"
       "hZ0HOFP5LvPNH8czo3ObNnN4qQ")#url變換

response = requests.get(url)
print(response.cookies)
html = BeautifulSoup(response.text)

title = html.find("title") #標題
#品牌、職業要變換
print(title)
f = open(str(title.text) + ".txt", "w", encoding="utf-8")

article = html.find("div", class_="indent") #職業需要變換 ＃內文
# find_all: list #直接用內文搜尋code
a = article.text
print(a)
sign = ["。","：", "/"]
for na in sign:

    a = a.replace(na, str(na)+"\n")
print(a)

f.write(str(a))
f.write(str(url))
f.close()

