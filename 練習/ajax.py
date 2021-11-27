import urllib.request as req
# 抓取網頁原始碼
url="https://medium.com/_/api/home-feed"

request=req.Request(url, headers={
  "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
})
with req.urlopen(request) as response:
  data=response.read().decode("utf-8")
import json
data=data.replace("])}while(1);</x>","")
data=json.loads(data)
print(data)
