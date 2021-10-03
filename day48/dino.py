from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_developer_path = "C:/Users/Satyam/Driver/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_developer_path)

url = "chrome://dino/"
driver.get(url)
# body = driver.find_element_by_css_selector("runner-canvas")
#
# while True:
#     body.send_keys(Keys.SPACE)
