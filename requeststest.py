#写一段代码用requests爬取网页数据
import requests
r = requests.get('https://www.douban.com/')
print(r.status_code)
print(r.cookies)
print(r.text)
print(r.content)
print(r.headers)
print(r.url)