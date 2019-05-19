### 基本使用

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
try:
    browser.get('http://www.baidu.com')
    input = browser.find_element_by_id('kw')
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser,10)
    wait.until(EC.presence_of_all_elements_located((By.ID,'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()
```

### 声明浏览器对象

```python
from selenium import webdriver browser = webdriver.Chrome()
browser = webdriver.Firefox()
browser = webdriver.Edge()
browser = webdriver.PhantomJS()
browser = webdriver.Safari()
```

### 访问页面

```python
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://www.taobao.com')
print(browser.page_source)
browser.close()
```

### 查找元素

#### 单元素

第一种

```python
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.taobao.com')
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first,input_second,input_third)
browser.close()
```

第二种

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get('http://www.taobao.com')
input_first = browser.find_element(By.ID,'q')
print(input_first)
browser.close()
```

#### 多元素

第一种

```python
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.taobao.com')
lis = browser.find_elements_by_css_selector('.service-bd li')
print(lis)
browser.close()
```

第二种

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get('http://www.taobao.com')
lis = browser.find_elements(By.CSS_SELECTOR,'.service-bd li')
print(lis)
browser.close()
```

### 元素交互

```python
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://www.taobao.com')

input = browser.find_element_by_id('q')
input.send_keys('Iphone')
time.sleep(1)
input.clear()
input.send_keys('iPad')
button = browser.find_element_by_class_name('btn-search')
button.click()
browser.close()
```

### 交互动作

```python
from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source= browser.find_element_by_css_selector('#draggable') # 拖拽对象
target= browser.find_element_by_css_selector('#droppable') # 拖拽目标

actions = ActionChains(browser)
actions.drag_and_drop(source,target)
actions.perform()
browser.close()
```

### 执行js代码

```python
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)') # 把下拉到最下面
browser.execute_script('alert("to bottom")')
browser.close()
```

### 获取元素信息

#### 获取属性

```python
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.get_attribute('class')) # 获取class
browser.close()
```

#### 获取文本值

```python
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
input = browser.find_element_by_css_selector('.zh-summary')
print(input.text)
browser.close()
```

#### 获取id,标签名,大小

```python
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
input = browser.find_element_by_class_name('zh-summary')
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)
browser.close()
```

#### Frame:进去和出来

```python
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')  # 进入里面iframe
source = browser.find_element_by_css_selector('#draggable') # 拖拽对象
print(source)
try:
    logo = browser.find_element_by_class_name('logo')
except NoSuchElementException:
    print('No Logo')
browser.switch_to.parent_frame() # 出来iframe
logo = browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)
```

### 等待

#### 隐式等待

```python
from selenium import webdriver
browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('https://www.zhihu.com/explore')
input = browser.find_element_by_class_name('zu-top-add-question')
print(input)
browser.close()
```

#### 显示等待

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://www.taobao.com/')
wait = WebDriverWait(browser,10)
input = wait.until(EC.presence_of_all_elements_located((By.ID,'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.btn-search')))
print(input,button)
browser.close()
```

### 前进和后退

```python
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
browser.get('http://www.taobao.com/')
browser.get('http://www.python.org/')
browser.back()  # 后退一步
time.sleep(1)
browser.forward() # 前进一步
browser.close()
```

### 设置cookie

```python
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())
browser.add_cookie({'name':'name','domain':'www.zhihu.com','value':'germey'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())
```

### 选项卡管理

```python
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.execute_script('window.open()') # 打开一个新的标签
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1]) # 切换标签
browser.get('https://www.taobao.com')
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])
browser.get('https://python.org')
```

### 异常处理

```python
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('请求超时')
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('没有此id')
finally:
    browser.close()
```

### 无头Chrome

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
 
# 创建一个参数对象，用来控制chrome以无界面模式打开
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

 
# 创建浏览器对象
browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
 
# 上网
url = 'http://www.baidu.com/'
browser.get(url)
time.sleep(3)
 
browser.save_screenshot('baidu.png') # 截图
 
browser.quit()
```

