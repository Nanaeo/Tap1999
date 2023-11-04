import base64
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

# 请填入Tap网页cookies 否则容易加载失败
def convert_cookies_to_dict(cookies):
    cookies = dict([larr.split("=", 1) for larr in cookies.split("; ")])
    return cookies


dictcookies = convert_cookies_to_dict("")
driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(412, 951)

driver.get('https://www.taptap.cn/')
for i in dictcookies:
    driver.add_cookie({"name": i[0], "value": i[1]})
time.sleep(5)
# https://www.taptap.cn/user/35246293/game-record/221062/module/2
driver.get('https://www.taptap.cn/user/122497384/game-record/221062/module/2')
time.sleep(5)
# 引发其进入小屏幕模式
driver.set_window_size(430, 980)
# 触发懒加载 实际上次数位置 列表截至有标志我没写
for i in range(1, 10):
    s = f'window.scrollBy(0,700)'  # 每次划700的单位
    driver.execute_script(s)  # 向下滚动，0在第一位是向上向下，0在第二位是向左向右，负号决定具体方向
    time.sleep(1.5)
    print(i)
# 获取真实的全高全宽
width = driver.execute_script("return document.documentElement.scrollWidth")
height = driver.execute_script("return document.documentElement.scrollHeight")
print(width, height)
# driver.execute_script('document.getElementsByClassName("taptap__main-header-content")[0].style.display = "none"')
driver.execute_script('document.documentElement.style.overflow = "hidden"')
# driver.execute_script('document.getElementsByClassName("app-record__user-contents")[0].style.borderRadius = "0 0 0 0"')
time.sleep(1)
driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride',
                       {'mobile': True, 'width': 430, 'height': height, 'deviceScaleFactor': 1})



# driver.set_window_size(width, height)

# 等待滚动条消失
time.sleep(5)

# 执行截图
res = driver.execute_cdp_cmd('Page.captureScreenshot', {'fromSurface': True})

# 返回的base64内容写入PNG文件
with open('221062.png', 'wb') as f:
    img = base64.b64decode(res['data'])
    f.write(img)

# 等待截图完成
driver.get_screenshot_as_file("test.png")
time.sleep(15)

# 关闭设备模拟
driver.execute_cdp_cmd('Emulation.clearDeviceMetricsOverride', {})
driver.quit()
