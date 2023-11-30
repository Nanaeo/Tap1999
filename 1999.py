import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(412, 951)

driver.get('https://www.taptap.cn/')
time.sleep(5)

# 解决白屏问题
driver.get('https://www.taptap.cn/user/122497384/game-record/221062/module/2')
time.sleep(5)

# 10次滑动 可根据dom元素动态处理
for i in range(1, 10):
    s = f'window.scrollBy(0,700)'  # 每次划700的单位
    driver.execute_script(s)  # 向下滚动，0在第一位是向上向下，0在第二位是向左向右，负号决定具体方向
    time.sleep(1.5)

width = driver.execute_script("return document.documentElement.scrollWidth")
height = driver.execute_script("return document.documentElement.scrollHeight")
print("width-height:", width, height)
# driver.execute_script('document.getElementsByClassName("taptap__main-header-content")[0].style.display = "none"')
driver.execute_script('document.documentElement.style.overflow = "hidden"')
time.sleep(1)
# 重置窗口大小
driver.set_window_size(width, height)

# 执行截图
time.sleep(5)
# 等待截图完成
driver.get_screenshot_as_file("test.png")
time.sleep(15)

# 关闭设备
driver.quit()

