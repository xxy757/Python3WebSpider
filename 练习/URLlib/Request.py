from urllib import request, parse
from utils import decode_response, print_response_info


# # 创建请求对象
# request = urllib.request.Request('https://baidu.com')

# # 发送请求
# response = urllib.request.urlopen(request)

# # 打印响应信息
# print_response_info(response)

# # 打印响应内容
# print("\n=== 响应内容 ===")
# print(decode_response(response))




url = 'http://httpbin.org/post'
headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {'name': 'Germey'}
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))

# # 获取响应内容（只能读取一次）
# content = decode_response(response)

# # 打印响应信息
# print_response_info(response)

# # 打印响应内容
# print("\n=== 响应内容 ===")
# print(content)