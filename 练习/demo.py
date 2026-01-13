import requests
# 写一个百度的请求
url = "https://www.baidu.com"
response = requests.get(url)
print(response.status_code)
