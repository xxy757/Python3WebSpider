"""
URLlib爬虫工具模块
包含常用的HTTP响应处理函数
"""

import gzip
import urllib.error
import socket


"""
解码HTTP响应内容，支持gzip压缩和多种编码

Args:
    response: urllib.response对象
    
Returns:
    str: 解码后的字符串内容
"""
def decode_response(response):
    """
    解码HTTP响应内容，支持gzip压缩和多种编码
    
    Args:
        response: urllib.response对象
        
    Returns:
        str: 解码后的字符串内容
    """
    # 读取响应内容
    content = response.read()    #response.read()只能读取一次！
    
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

"""
安全的URL打开函数，包含异常处理

Args:
    url: 请求的URL
    data: POST数据
    timeout: 超时时间（秒）
    **kwargs: 其他参数

Returns:
    tuple: (success, result_or_error)
"""
def safe_urlopen(url, data=None, timeout=10, **kwargs):
    """
    安全的URL打开函数，包含异常处理
    
    Args:
        url: 请求的URL
        data: POST数据
        timeout: 超时时间（秒）
        **kwargs: 其他参数
        
    Returns:
        tuple: (success, result_or_error)
    """
    try:
        if data:
            response = urllib.request.urlopen(url, data=data, timeout=timeout, **kwargs)
        else:
            response = urllib.request.urlopen(url, timeout=timeout, **kwargs)
        
        content = decode_response(response)
        return True, content
        
    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            return False, "请求超时，请检查网络连接或增加超时时间"
        else:
            return False, f"请求失败: {e}"
    except Exception as e:
        return False, f"发生错误: {e}"


def get_response_info(response):
    """
    获取HTTP响应的详细信息
    
    Args:
        response: urllib.response对象
        
    Returns:
        dict: 包含响应信息的字典
    """
    return {
        'url': response.url,
        'status': response.status,
        'headers': dict(response.headers),
        'reason': response.reason if hasattr(response, 'reason') else None
    }


def print_response_info(response):
    """
    打印HTTP响应的基本信息
    
    Args:
        response: urllib.response对象
    """
    info = get_response_info(response)
    print("=== HTTP响应信息 ===")
    print(f"URL: {info['url']}")
    print(f"状态码: {info['status']}")
    print(f"状态描述: {info['reason']}")
    print("响应头:")
    for key, value in info['headers'].items():
        print(f"  {key}: {value}")
    print("===================")