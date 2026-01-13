"""
requests库使用示例
相比urllib更简洁、更强大
"""

import requests

# 1. 基本GET请求
print("=== 基本GET请求 ===")
response = requests.get('https://httpbin.org/get')
print(f"状态码: {response.status_code}")
print(f"响应内容: {response.text[:200]}...")  # 只显示前200字符

# 2. 带参数的GET请求
print("\n=== 带参数的GET请求 ===")
params = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('https://httpbin.org/get', params=params)
print(f"请求URL: {response.url}")
print(f"JSON响应: {response.json()}")

# 3. POST请求
print("\n=== POST请求 ===")
data = {'name': 'Germey', 'age': 25}
response = requests.post('https://httpbin.org/post', data=data)
print(f"状态码: {response.status_code}")
print(f"响应JSON: {response.json()}")

# 4. 设置请求头
print("\n=== 设置请求头 ===")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Referer': 'https://httpbin.org/'
}
response = requests.get('https://httpbin.org/get', headers=headers)
print(f"请求头信息: {response.json()['headers']}")

# 5. 错误处理
print("\n=== 错误处理示例 ===")
try:
    response = requests.get('https://httpbin.org/status/404', timeout=5)
    response.raise_for_status()  # 如果状态码不是200，抛出异常
    print("请求成功")
except requests.exceptions.HTTPError as e:
    print(f"HTTP错误: {e}")
except requests.exceptions.RequestException as e:
    print(f"请求异常: {e}")

# 6. 会话保持（保持Cookie）
print("\n=== 会话保持 ===")
session = requests.Session()
# 第一次请求设置Cookie
response1 = session.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
# 第二次请求会自动携带Cookie
response2 = session.get('https://httpbin.org/cookies')
print(f"Cookie信息: {response2.json()}")

print("\n=== requests库功能演示完成 ===")