# #快速上手
import requests

# # 发送get请求
# r = requests.get('https://api.github.com/events')
# # 发送post请求
# r = requests.post('http://httpbin.org/post', data={'key':'value'})
#
# # 传递URL参数
# # 通过使用params关键字参数，可以提供一个字符串字典。
# # 比如传递key1=value1和key2=value2
# payload = {'key1':'value1', 'key2':'value2'}
# r = requests.get('http://httpbin.org/get', params=payload)
# print(r.url) # http://httpbin.org/get?key1=value1&key2=value2
#
# #也可以将一个列表作为值传入
# payload = {'key1':'value1', 'key2':['value2', 'value3']}
# r = requests.get("http://httpbin.org/get", params=payload)
# print(r.url) #http://httpbin.org/get?key1=value1&key2=value2&key2=value3
#
#
# #响应内容
# # 读取响应内容-文本格式
# r = requests.get('https://api.github.com/events')
# print(r.text)
# # Requests 会自动解码来自服务器的内容。大多数 unicode 字符集都能被无缝地解码。
# # 请求发出后，Requests 会基于 HTTP 头部对响应的编码作出有根据的推测。
# # 可以通过r.encoding = 'ISO-8859-1'来改变编码格式
# #当再次调用r.text的时候都将使用新的编码格式
#
# #二进制响应内容
# print(r.content)
# #Requests 会自动为你解码 gzip 和 deflate 传输编码的响应数据。
# #举例 以请求返回的二进制数据创建一张图片
# '''
# from PIL import Image
# from io import BytesIO
# i = Image.open(BytesIO(r.content))
# '''
#
# #JSON响应内容
# r = requests.get("https://api.github.com/events")
# print(r.json())
# # 如果JSON解析失败会抛出异常
# #成功调用r.json()并不意味返回了正常结果，有时需要对节点或状态码进行校验，可以调用r.raise_for_status()或检查r.status_code()
#
# # 原始响应内容
# # 很少见的情况下，可能需要获取原始套接字响应，此时必须保证在初始请求中设置了stream=True
# r = requests.get('https://api.github.com/events', stream = True)
# print(r.raw)
# #将文件流保存到文件
# '''
# with open(filename, 'wb') as fd:
#     for chunk in r.iter_content(chunk_size):
#         fd.write(chunk)
# '''
#
#
#
# # 定制请求头
# # 通过给参数headers传递一个字典来实现即可
# url = 'https://api.github.com/some/endpoint'
# headers = {'user-agent':'my-app/0.0.1'}
# r = requests.get(url, headers = headers)
# #自定义的header优先级低于某些特定的信息源，比如
# #如果在 .netrc 中设置了用户认证信息，使用 headers= 设置的授权就不会生效。而如果设置了 auth= 参数，``.netrc`` 的设置就无效了。
# #如果被重定向到别的主机，授权 header 就会被删除。
# #代理授权 header 会被 URL 中提供的代理身份覆盖掉。
# #在我们能判断内容长度的情况下，header 的 Content-Length 会被改写。
#
# #Requests 不会基于自定义 header 的具体情况改变自己的行为。只不过在最后的请求中，所有的 header 信息都会被传递进去。
# #注意: 所有的 header 值必须是 string、bytestring 或者 unicode。
#
# # 更加复杂的POST请求
# # 发送表单数据
# # 传递一个字典给data
# payload = {'key1':'value1', 'key2': 'value2'}
# r = requests.post('http://httpbin.org/post', data=payload)
# print(r.text)
# '''
#   "form": {
#     "key1": "value1",
#     "key2": "value2"
#   }, '''
#
# # 或者传递元组列表，可以用来处理一个key有多个value的情况
# payload = [('key1','value1'), ('key1', 'value2')]
# r = requests.post('http://httpbin.org/post', data=payload)
# print(r.text)
# '''
#   "form": {
#     "key1": [
#       "value1",
#       "value2"
#     ]
#   },
# '''
#
# # 如果传递string，那么就会将其作为报文发送出去
# import json
# url = 'https://api.github.com/some/endpoint'
# payload = {'some': 'data'}
# r = requests.post(url, data=json.dumps(payload))
#
# # 更简单的传递json的方式是用json关键字参数, 可以自动编码为json
# url = 'https://api.github.com/some/endpoint'
# payload = {'some': 'data'}
# r = requests.post(url, json=payload)
#
# # POST一个多部分编码(Multipart-Encoded)的文件
# url = 'http://httpbin.org/post'
# files = {'file':open('report.xls', 'rb')}
# r = requests.post(url, files = files)
# print(r.text)
# '''
#   "files": {
#     "file": "data:application/octet-stream;base64,suLK1NK7z8INCg=="
#   },
# '''
# # 可以指定文件名，文件类型和请求头
# files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
# r = requests.post(url, files = files)
#
# #也可以发送作为文件来接收的字符串
# files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}
# r = requests.post(url, files = files)
#

# 响应状态码
r = requests.get('http://httpbin.org/get')
print(r.status_code)
# 可以使用内置状态码查询对象
print(r.status_code == requests.codes.ok)

# 如果发送了一个错误请求（4xx客户端错误，5xx服务器响应错误），我们可以通过Respons.raise_for_status()来抛出异常
bad_r = requests.get('http://httpbin.org/status/404')
print(bad_r.status_code)
try:
    bad_r.raise_for_status()
except Exception as e:
    print(e)

# 响应头
# requests模块以python字典的形式返回响应头
print(
    r.headers)  # {'Date': 'Fri, 19 Feb 2021 09:12:20 GMT', 'Content-Type': 'application/json', 'Content-Length': '307', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}
# 但是这个字典比较特殊：它是仅为 HTTP 头部而生的。根据 RFC 2616， HTTP 头部是**大小写不敏感**的。
# 所以可以同任意大写形式来获取响应头字段
print(r.headers['content-type'])
print(r.headers['Content-Type'])
# 它还有一个特殊点，那就是服务器可以多次接受同一 header，每次都使用不同的值。但 Requests 会将它们合并，这样它们就可以用一个映射来表示出来，参见 RFC 7230:
# A recipient MAY combine multiple header fields with the same field name into one "field-name: field-value" pair, without changing the semantics of the message, by appending each subsequent field value to the combined field value in order, separated by a comma.
# 接收者可以合并多个相同名称的 header 栏位，把它们合为一个 "field-name: field-value" 配对，将每个后续的栏位值依次追加到合并的栏位值中，用逗号隔开即可，这样做不会改变信息的语义。

# Cookie
# 如果某个响应中包含一些cookie可以快速访问他们
# r.cookies['example_cookie_name']
# 如果想发送cookie到服务器 可以使用cookies参数
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
r.text
'{"cookies": {"cookies_are": "working"}}'

# Cookie 的返回对象为 RequestsCookieJar，它的行为和字典类似，但接口更为完整，适合跨域名跨路径使用。你还可以把 Cookie Jar 传到 Requests 中：
jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
url = 'http://httpbin.org/cookies'
r = requests.get(url, cookies=jar)
r.text

# 重定向和请求历史
# 默认情况下，除了 HEAD, Requests 会自动处理所有重定向。
#
# 可以使用响应对象的 history 方法来追踪重定向。
#
# Response.history 是一个 Response 对象的列表，为了完成请求而创建了这些对象。这个对象列表按照从最老到最近的请求进行排序。
# 例如，Github 将所有的 HTTP 请求重定向到 HTTPS：
r = requests.get('http://github.com')
print(r.url)
print(r.status_code)
print(r.history)

# 如果你使用的是GET、OPTIONS、POST、PUT、PATCH 或者 DELETE，那么你可以通过 allow_redirects 参数禁用重定向处理：
r = requests.get('http://github.com', allow_redirects=False)
print(r.status_code)

# 如果你使用了 HEAD，你也可以启用重定向：
r = requests.head('http://github.com', allow_redirects=True)
print(r.url)

# 超时
# 通过timeout参数设置超时时间，超过后停止等待响应，基本上所有的生产代码都应该使用这一参数
requests.get('http://github.com', timeout=0.001)
#注意：timeout参数仅对连接时的过程有效，而和响应报文的下载无关。timeout并不是整个响应下完的时间限制，而是如果服务器没有在timeout内响应，将会抛出一个异常

#错误与异常
#遇到网络问题（如：DNS 查询失败、拒绝连接等）时，Requests 会抛出一个 ConnectionError 异常。
#
#如果 HTTP 请求返回了不成功的状态码， Response.raise_for_status() 会抛出一个 HTTPError 异常。
#
#若请求超时，则抛出一个 Timeout 异常。
#
#若请求超过了设定的最大重定向次数，则会抛出一个 TooManyRedirects 异常。
#
#所有Requests显式抛出的异常都继承自 requests.exceptions.RequestException 。
