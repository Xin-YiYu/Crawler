import requests
from bs4 import BeautifulSoup

url = "https://buzzorange.com/techorange/2017/09/05/2017-best-learning-resources/"  #url變換

response = requests.get(url, cookies={"has_pager": "1"})
# print(response.cookies)
html = BeautifulSoup(response.text)
#print(html)

title = html.find("h1", class_="entry-title")  #標題
# 品牌、職業要變換
# print(title.text)
f = open(str(title.text) + ".txt", "w", encoding="utf-8")
title = html.find_all("div", class_="entry-content")
#print(title)

r1 = []
r2 = []
for t in title:
    aa = t.find_all("a")
    z = t.find_all("p")
    b = z[0:19]
    #print(aa)
    for a1 in aa:
        a2 = a1["href"]
        r2.append(a2)

    for c in b:
        d = c.text
        r1.append(d)

r_1= r1[5:20] #text:14
r_2= r2[0:11] #web:11

r_1[0] = r_1[0] + r_1[1]
del(r_1[1])
r_1[4] = r_1[4] + r_1[5]
del(r_1[5], r_1[6])
print(r_1)
print(len(r_1))

for x, y in zip(r_1, r_2):
    f.write(str(x))
    f.write("\n")
    f.write(str(y))
    f.write("\n")
    f.write("\n")

f.write("\n")
f.write("url= " + url)
f.close()


