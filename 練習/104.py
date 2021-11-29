import urllib.request as req
# 抓取網頁原始碼
def getData(url):
  request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
  })
  with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div", class_="title")
    for title in titles:
      if title.a != "None":
        print(title.a.string)
    nextlink=root.find("a", string="‹ 上頁")
    return nextlink["href"]
pageURL="https://www.104.com.tw/jobs/main/"
count=0
while count<3:
  pageURL="https://www.104.com.tw/jobs/main/"+getData(pageURL)
  count+=1