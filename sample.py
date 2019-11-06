import requests
from bs4 import BeautifulSoup

start = 3062
howmany = 10
result = []

for i in range(howmany):
    url = "https://www.ptt.cc/bbs/Beauty/index" + str(start-i) + ".html"
    print(url)
    respones = requests.get(url, cookies={"over18":"1"})
    html = BeautifulSoup(respones.text)
    title = html.find_all("div", class_="title")# list
    print(title)
    for t in title: # 走過再拿出盒子
        a = t.find("a")
        if not a == None:
            article = "https://www.ptt.cc/" +a["href"]
            add = {
            "title": a.text,
            "url": article,
            }
            result.append(add)

        print(a)
print(result)