from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_developer_path = "C:/Users/Satyam/Driver/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_developer_path)
url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(url)

number = driver.find_element_by_css_selector("#articlecount a")
# number.click()
# print(driver.find_element_by_css_selector("h1").text)
search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# driver.close()
