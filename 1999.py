import base64
import time
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options


def convert_cookies_to_dict(cookies):
    cookies = dict([larr.split("=", 1) for larr in cookies.split("; ")])
    return cookies


dictcookies = convert_cookies_to_dict("")
driver = webdriver.Edge()
driver.set_window_size(412, 951)

driver.get('https://www.taptap.cn/')
for i in dictcookies:
    driver.add_cookie({"name": i[0], "value": i[1]})
time.sleep(5)
driver.get('https://www.taptap.cn/user/35246293/game-record/221062')
time.sleep(5)

width = driver.execute_script("return document.documentElement.scrollWidth")
height = driver.execute_script("return document.documentElement.scrollHeight")
print(width, height)
# driver.set_window_size(width, height)
driver.execute_script('document.getElementsByClassName("taptap__main-header-content")[0].style.display = "none"')
driver.execute_script('document.documentElement.style.overflow = "hidden"')
driver.execute_script('document.getElementsByClassName("app-record__user-contents")[0].style.borderRadius = "0 0 0 0"')
time.sleep(1)

driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride',
                       {'mobile': False, 'width': width, 'height': height, 'deviceScaleFactor': 1})

# 执行截图
res = driver.execute_cdp_cmd('Page.captureScreenshot', {'fromSurface': True})

# 返回的base64内容写入PNG文件
with open('221062.png', 'wb') as f:
    img = base64.b64decode(res['data'])
    f.write(img)

# 等待截图完成
time.sleep(15)

# 关闭设备模拟
driver.execute_cdp_cmd('Emulation.clearDeviceMetricsOverride', {})
# driver.get_screenshot_as_file("221062.png")
driver.quit()
