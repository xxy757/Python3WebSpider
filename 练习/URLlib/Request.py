import urllib.request  
from utils import decode_response, print_response_info


# 创建请求对象
request = urllib.request.Request('https://python.org')  

# 发送请求
response = urllib.request.urlopen(request)  

# 打印响应信息
print_response_info(response)

# 打印响应内容
print("\n=== 响应内容 ===")
print(decode_response(response))