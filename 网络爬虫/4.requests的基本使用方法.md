## requests的基本使用方法

#### 实例

```python
import requests
res = requests.get('http://www.baidu.com')
print(type(res))  # 获取一个对象
print(res.status_code)  # 获取状态码
print(type(res.text)) # 获取页面
print(type(res.cookies)) # 获取cookie
```

#### 请求方式

- requests.get() 
- requests.post()
- requests.put()
- requests.patch()
- requests.options()
- requests.head()
- requests.delete()

#### 获取数据

- res.json() :获取json数据
- res.text:获取文本信息
- res.content :获取二进制数据

#### 响应

#### response的属性

- status_code :获取状态码
- text:获取文本信息
- headers:获取头部信息
- content:获取二进制数据
- cookies:获取cookie
- url:访问的url
- history:历史记录

### 高级操作

#### 文件上传

```python
import requests
files = {'file':open('11.jpg','rb')}
requests.post('url',files=files)
```

#### 获取cookie

```python
res.cookies.item()
```

#### 会话维持

```python
import requests
session = requests.session()
session.get('http://httpbin.org/cookies/set/number/1000000')
res = session.get('http://httpbin.org/cookies')
print(res.text)
```

#### 代理设置

```python
import requests
proxies = {
    'http':'http://127.0.0.1:5000'
}
res = requests.get('http://www.baidu.com',proxies=proxies)
```

#### 超时设置

```python
from requests.exceptions import ReadTimeout
import requests
try:
    res = requests.get('http://www.baidu.com',timeout=0.01)
    print(res.text)
except ReadTimeout:
    print(111)
```

#### 认证设置:auth

```python
res = requests.get('http://www.baidu.com',auth={'user':123})
```

#### 异常处理

```python
from requests.exceptions import ReadTimeout, HTTPError,RequestException
ReadTimeout:超时
HTTPError:
ConnectionError:网络不通
RequestException
```

