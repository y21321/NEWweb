# 抓取PTT電影版網頁標題
import urllib.request as req
url="https://www.ptt.cc/bbs/Lifeismoney/index.html"
# 建立request物件，附加 Reaquest header資訊
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Mobile Safari/537.36"
})
# 使用request物件抓取的資料使用urlopen()打開，讀取並解析成utf-8
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
print(data)
# 解析原始碼，找到網頁文章標題
import bs4
root=bs4.BeautifulSoup(data,"lxml")
titles=root.find_all("div",class_="title") # 找到所有有 class="title"的div標籤
for title in titles:
    if title.a != None: # 如果標題包含a標籤（文章未被刪除），印出來
        print(title.a.string)