import os
import sys
from selenium import webdriver

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


# enter your id and password here!
USER = "id"
PASS = "pass"

browser = webdriver.Chrome("../webdriver/chromedriver")
browser.implicity_wait(3)

url_login = "https://nid.naver.com/nidlogin.login"
browser.get(url_login)
print("Opening a login page...")

e = browser.find_element_by_id("id")
e.clear()
e.send_keys(USER)
e = browser.find_element_by_id("pw")
e.clear()
e.send_keys(PASS)

form = browser.find_element_by_css_selector("input.btn_global[type=submit]")
form.submit()
print("Clicking a login button...")

# get information from shopping page
browser.get("https://order.pay.naver.com/home?tabMenu=SHOPPING")

products = browser.find_element_by_css_selector(".p_info span")
print(products)
for product in products:
  print("-", product.text)
