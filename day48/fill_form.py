from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_developer_path = "C:/Users/Satyam/Driver/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_developer_path)

url = "http://secure-retreat-92358.herokuapp.com/"
driver.get(url)

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Sat")

last_name = driver.find_element_by_name("lName")
last_name.send_keys("Bal")

email_id = driver.find_element_by_name("email")
email_id.send_keys("satybal@gmail.com")
email_id.send_keys(Keys.ENTER)

button = driver.find_elements_by_css_selector("form button")
button.click()

# driver.quit()
