from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# def isElementExist(d):
#     flag = True
#     browser = d
#     try:
#         browser.find_element_by_class("pwd-login-link")
#         return flag
#     except:
#         flag = False
#         return flag

target = "999"
driver = webdriver.Chrome()
driver.get("https://m.tb.cn/h.fNCbCeN?tk=D8az2fihwKA")
# driver.get("https://www.baidu.com")
time.sleep(2)


# pwd-login-link 用户名密码登录
# fm-login-id 账号
# fm-login-password 密码
# fm-button fm-submit password-login  class 登录
# fm-agreement-checkbox 同意协议


iframe_eles = driver.find_elements(By.TAG_NAME, "iframe")
has_iframe = False
if iframe_eles:
    print("有弹框")
    has_iframe = True


if has_iframe:
    driver.switch_to.frame(driver.find_elements(By.TAG_NAME, "iframe")[0])
    sms_text_ele = driver.find_element_by_class_name("master-login-title")
    print(sms_text_ele.text)
    pwd_login_ele = driver.find_element_by_class_name("pwd-login-link")
    pwd_login_ele.click()
    time.sleep(2)
    driver.find_element_by_id("fm-login-id").send_keys("zjxht62")
    time.sleep(2)
    driver.find_element_by_id("fm-login-password").send_keys("c9r6e2h7ZJX")
    time.sleep(2)
    driver.find_element_by_id("fm-agreement-checkbox").click()
    driver.find_element_by_class_name("fm-button fm-submit password-login").click()



# try:
#     # ele = driver.find_element_by_class_name("master-login-title")
#     ele = driver.find_element_by_css_selector("#login > div.master-login-title")
#     print("找到元素", ele.text)
#     need_login = True
#
# except Exception as e:
#     print("未找到元素", e)
#     need_login = False
#
# print(need_login)


# login_ele = driver.find_element_by_id("fm-sms-login-id")

price_ele = driver.find_element(By.CSS_SELECTOR, "#root > div > div.rax-view-v2.Detail--container--17hcFL4 > div > div.rax-view-v2.normal--descCollpaseContainer--228MYrV > div.rax-view-v2.priceMod--priceMod--Yld0tWj > div > div.rax-view-v2.priceMod--priceTextWrap--3PwMboh > span.rax-text-v2.priceMod--soldPrice--20BWwRm")

#root > div > div.rax-view-v2.Detail--container--17hcFL4 > div > div.rax-view-v2.normal--descCollpaseContainer--228MYrV > div.rax-view-v2.priceMod--priceMod--Yld0tWj > div > div.rax-view-v2.priceMod--priceTextWrap--3PwMboh > span.rax-text-v2.priceMod--soldPrice--20BWwRm
#root > div > div.rax-view-v2.Detail--container--17hcFL4 > div > div.rax-view-v2.normal--descCollpaseContainer--228MYrV > div.rax-view-v2.priceMod--priceMod--Yld0tWj > div > div.rax-view-v2.priceMod--priceTextWrap--3PwMboh > span.rax-text-v2.priceMod--soldPrice--20BWwRm


print(price_ele.text==target)
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
driver.close()
