"""
GET请求参数详细演示
"""

import requests

print("=== GET请求参数演示 ===\n")

# 1. 基本参数传递
print("1. 基本参数传递")
params = {
    'name': '张三',
    'age': 25,
    'city': '北京'
}
response = requests.get('https://httpbin.org/get', params=params)
print(f"最终URL: {response.url}")
print(f"服务器接收到的参数: {response.json()['args']}")
print()

# 2. 参数自动URL编码
print("2. 参数自动URL编码")
params = {
    'search': 'Python 爬虫教程',
    'category': '编程/技术',
    'price': '100-200元'
}
response = requests.get('https://httpbin.org/get', params=params)
print(f"最终URL: {response.url}")
print("注意：空格被编码为%20，中文被正确编码")
print()

# 3. 列表参数（多个相同参数名）
print("3. 列表参数（多个相同参数名）")
params = {
    'tags': ['python', '爬虫', '教程'],
    'colors': ['red', 'blue']
}
response = requests.get('https://httpbin.org/get', params=params)
print(f"最终URL: {response.url}")
print(f"服务器接收到的参数: {response.json()['args']}")
print("注意：列表参数会自动展开为多个同名参数")
print()

# 4. 复杂参数结构
print("4. 复杂参数结构")
params = {
    'filter': {
        'price': {'min': 100, 'max': 500},
        'category': 'electronics',
        'in_stock': True
    },
    'sort': 'price_desc',
    'page': 1
}
response = requests.get('https://httpbin.org/get', params=params)
print(f"最终URL: {response.url}")
print(f"服务器接收到的参数: {response.json()['args']}")
print("注意：复杂结构会被转换为字符串")
print()

# 5. 实际网站示例（模拟搜索）
print("5. 实际网站示例（模拟百度搜索）")
params = {
    'wd': 'Python爬虫教程',
    'ie': 'utf-8'
}
# 注意：实际百度搜索需要更多参数和headers
response = requests.get('https://httpbin.org/get', params=params)
print(f"模拟搜索URL: {response.url}")
print("在实际网站中，这种参数用于搜索、筛选、分页等功能")
print()

# 6. 参数与URL拼接对比
print("6. 手动拼接 vs params参数对比")
base_url = 'https://httpbin.org/get'

# 方式1：手动拼接（容易出错）
manual_url = base_url + '?name=李四&age=30&city=上海'
response1 = requests.get(manual_url)

# 方式2：使用params参数（推荐）
params = {'name': '李四', 'age': 30, 'city': '上海'}
response2 = requests.get(base_url, params=params)

print(f"手动拼接URL: {manual_url}")
print(f"params生成URL: {response2.url}")
print("两者结果相同，但params方式更安全、更易维护")
print()

print("=== GET参数总结 ===")
print("✅ GET请求可以带参数，通过URL查询字符串传递")
print("✅ requests的params参数会自动处理URL编码")
print("✅ 支持字典、列表等复杂数据结构")
print("✅ 比手动拼接URL更安全、更易维护")
print("✅ 广泛应用于搜索、筛选、分页、API调用等场景")