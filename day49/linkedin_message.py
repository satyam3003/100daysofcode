from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

executable_path = "C:/Users/Satyam/Driver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=executable_path)

url = "https://www.linkedin.com/messaging/thread/2-MzI4NzU4MzgtYzFhMi00ODJkLWE2YWEtYmNkOGI2YmExNmZiXzAxMA==/"

driver.get(url)

sign_in = driver.find_element_by_link_text("Sign in")
sign_in.click()

email = driver.find_element_by_name("session_key")
email.send_keys("")

email = driver.find_element_by_id("password")
email.send_keys("")

button = driver.find_element_by_css_selector("div .login__form_action_container button")
button.click()

time.sleep(5)

smogg = driver.find_elements_by_css_selector('.msg-conversation-listitem')[0]
smogg.click()

message = driver.find_element_by_css_selector(".flex-grow-1 .msg-form__contenteditable")
message.send_keys(
    "Madhura ka brain hang hora")
message.send_keys(Keys.ENTER)

time.sleep(10)
send = driver.find_element_by_css_selector("div.msg-form__right-actions  button")  # .msg-form__send-button
send.click()
