from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime

chrome_developer_path = "C:/Users/Satyam/Driver/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_developer_path)

url = "https://orteil.dashnet.org/cookieclicker/"
driver.get(url)
cookie = driver.find_element_by_id("bigCookie")

while True:
    cookie.click()
    now = int(datetime.datetime.now().strftime("%S"))
    print(now)
    if now % 5 == 0:
        items = driver.find_elements_by_css_selector(".unlocked")
        items.reverse()
        for item in items:
            try:
                item.click()
            except:
                continue
