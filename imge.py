import requests
from bs4 import BeautifulSoup
import os

url = "https://www.commonhealth.com.tw/blog/blogTopic.action?nid=1108&utm_source=chfacebook&utm_medium=social&utm_campaign=dailypost-10-03-editor&fbclid=IwAR24uvIyhu7Q_DSt65yr1q79y9KPErtcRu5jfp1QHxlUjR8i2dFK91tMOm0"
# cookies: 同一個網址 在不同時間或者不同地方給你不一樣的回應
# 例子: 自動登入(www.facebook.com)
response = requests.get(url, cookies={"over18":"1"})
# 如果是用requests工具, 拿到網頁 .text
html = BeautifulSoup(response.text)
#print(html)

dn = "For the better life"
if not os.path.exists(dn):
  os.makedirs(dn)

x = html.find("div", class_="essay__editor editorBlock")
img = x.find_all("img")
#.find_all變成list
print(img)

fs = ["jpg", "jpeg", "gif", "png"]
for a in img:
  sub = a["src"]
  img_url = sub
  print(img_url)

  y = "https:" + str(img_url) #拿到圖片網址
  r = requests.get(y,
                   stream=True,
                   verify=False) #下載
  #print(y)
  img_name = dn + "/" + a["src"].split("/")[-1]
  #print(img_name)
  # 開啟檔案:
  # 純文字: "r", "w" + encoding
  # 非純文字: "rb", "wb"
  f = open(img_name, "wb")
  # requests模組: .text(純文字) .raw(檔案)(get stream=True)
  img = r.raw.read()
  f.write(img)
  f.close()
  # os.remove(str(title.text) + ".txt") #刪除當下資料夾文件