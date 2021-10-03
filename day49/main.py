from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

PHONE = "8983517226"

executable_path = "C:/Users/Satyam/Driver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=executable_path)

url = "https://www.linkedin.com/jobs/search/?f_AL=true&f_WRA=true&geoId=92000000&keywords=marketing%20intern&location=Worldwide"

driver.get(url)

sign_in = driver.find_element_by_link_text("Sign in")
print("apply_click")
sign_in.click()

email = driver.find_element_by_name("session_key")
email.send_keys("baldawasatyam30@gmail.com")

email = driver.find_element_by_id("password")
email.send_keys("Satyam@30")

button = driver.find_element_by_css_selector("div .login__form_action_container button")
button.click()

time.sleep(5)

all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    # Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        # If phone field is empty, then fill your phone number.
        # phone = driver.find_element_by_class_name("fb-single-line-text__input")
        # if phone.text == "":
        #     phone.send_keys(PHONE)

        submit_button = driver.find_element_by_css_selector("footer button")

        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
