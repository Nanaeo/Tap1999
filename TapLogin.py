import base64
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.set_window_size(412, 951)
driver.get("https://accounts.taptap.cn/login")
time.sleep(5)
driver.find_element(By.CLASS_NAME, "icon-ico-m32-w32-QQ").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "confirm-footer__button").click()
time.sleep(2)
# 进入iframe
driver.switch_to.frame("ptlogin_iframe")
time.sleep(2)
# 输出Qrcode
driver.find_element(By.CSS_SELECTOR, ".qrImg").screenshot('Qrcode.png')
time.sleep(10)
