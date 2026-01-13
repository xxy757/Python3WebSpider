import urllib.request
import urllib.error
import gzip
import socket

# urlopen函数解析
# def urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
#             *, cafile=None, capath=None, cadefault=False, context=None):
# urlopen函数用于打开一个URL，返回一个响应对象
# 参数：
#     url: 要打开的URL字符串
#     data: 可选的POST数据，用于POST请求
#     timeout: 可选的超时时间，单位为秒
#     cafile: 可选的CA证书文件路径
#     capath: 可选的CA证书目录路径
#     cadefault: 可选的是否使用默认CA证书，默认为False
#     context: 可选的SSL上下文对象，用于自定义SSL连接
# 返回值：
#     一个响应对象，包含服务器返回的响应内容、状态码、响应头等信息



response = urllib.request.urlopen('https://www.baidu.com')
# print(decode_response(response)) #打印响应内容
# print(type(response))
# print(response.status)   #打印http状态码
# print(response.getheaders())  #打印所有响应头
# print(response.getheader('Server')) #打印Server响应头

# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')   #设置POST请求参数
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)  
# print(response.read())



# 超时爬虫
try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=10)  
    print(response.read())
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print("请求超时，请检查网络连接或增加超时时间")
    else:
        print(f"请求失败: {e}")
except Exception as e:
    print(f"发生错误: {e}")


# 根据响应头判断是否需要解压，并尝试多种编码方式
def decode_response(response):
    # 读取响应内容
    content = response.read()
    
    # 检查是否gzip压缩
    if response.headers.get('Content-Encoding') == 'gzip':
        content = gzip.decompress(content)
    
    # 尝试多种编码方式
    encodings = ['utf-8', 'gbk', 'gb2312', 'iso-8859-1']
    
    for encoding in encodings:
        try:
            return content.decode(encoding)
        except UnicodeDecodeError:
            continue
    
    # 如果所有编码都失败，返回原始字节
    return content


