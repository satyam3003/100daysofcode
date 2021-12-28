from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

CHROME_DRIVER_PATH = "C:/Users/Satyam/Driver/chromedriver.exe"
INSTA_ID = ""
INSTA_PASSWORD = ""
INSTA_URL = "https://www.instagram.com/natgeo/followers/"


class InstagramFollowing:
    def __init__(self, id_insta, pass_word, url):
        self.id = id_insta
        self.password = pass_word
        self.url = url
        self.counter = 0
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.driver.get(url)

    def insta_login(self):
        time.sleep(1)
        log_in_u_id = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        log_in_u_id.send_keys(self.id)

        password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(self.password)

        time.sleep(1)
        log_in = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        log_in.click()

        time.sleep(2)
        try:
            not_now = self.driver.find_element_by_css_selector(".cmbtv button")
            not_now.click()

        except NoSuchElementException:
            pass

    def insta_follow(self):
        time.sleep(2)
        followers_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers_button.click()
        play = True

        while play:
            follow_list = self.driver.find_elements_by_css_selector(".PZuss li button")
            print(len(follow_list))
            for follow in follow_list:
                if follow.text == 'Follow':
                    try:
                        follow.click()
                        # time.sleep(0.5)
                        self.counter += 1
                        print(self.counter)
                        if self.counter > 1000:
                            play = False
                    except:
                        pass

# STEP 1: INITIALIZATION
follow_natgeo = InstagramFollowing(INSTA_ID, INSTA_PASSWORD, INSTA_URL)
print("initialization done")

# STEP 2: LOGIN
follow_natgeo.insta_login()
print("login...done")

# STEP 3: Follow
# follow_natgeo.insta_follow()
print("following done..")
