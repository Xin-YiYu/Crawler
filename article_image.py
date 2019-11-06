
import requests
from bs4 import BeautifulSoup
import os

result = []
url = "https://pb.ps-taiwan.org/catalog/ins.php?index_m1_id=1&index_id=495&fbclid=IwAR3W1oNulsll9RwXg1YTll7NRfz7MnPAxlDu2DjOmR8WEjOYAviUEvK8b9A"
response = requests.get(url, cookies={"has_pager": "1"})
html = BeautifulSoup(response.text)
title = html.find("h3", class_="articleTitle")

dn = str(title.text)
if not os.path.exists(dn):
    os.makedirs(dn)

x = html.find("div", class_="textEditor")
img = x.find_all("img")

# .find_all變成list
# print(img)

fs = ["jpg", "jpeg", "gif", "png"]
for a in img:
    sub = a["src"]
    img_url = sub
    #print(img_url)
    y = "https://pb.ps-taiwan.org/" + str(img_url) # 拿到圖片網址
    r = requests.get(y,
                    stream=True,
                    verify=False) # 下載圖片
    #print(y)
    img_name = dn + "/" + a["src"].split("/")[-1]
    # print(img_name)
    # 開啟檔案:
    # 純文字: "r", "w" + encoding
    # 非純文字: "rb", "wb"
    f = open(img_name, "wb")
#   requests模組: .text(純文字) .raw(檔案)(get stream=True)
    img = r.raw.read()
    f.write(img)
    f.close()

text_name = dn + "/" + str(title.text) + ".txt" # text path
f = open(text_name, "w", encoding="utf-8")
article = html.find("li", id="intro")
# find_all: list
#print(article)
a = article.text
#print(a)
sign = ["。", "：", "/", "，"]
for na in sign:
    a = a.replace(na, str(na)+"\n")
    #print (a)


f.write(a)
f.write(str(url))
f.close()
# os.remove(str(title.text) + ".txt") #刪除當下資料夾文件

