import urllib.request
""" 以get请求方式获取网页内容 """

# 打开指定需要爬取的网页
response = urllib.request.urlopen('http://www.baidu.com')
# 读取网页代码
html = response.read()
print(html)
