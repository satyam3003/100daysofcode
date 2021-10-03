from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

CHROME_DRIVER_PATH = "C:/Users/Satyam/Driver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}

response = requests.get(
    "https://www.zillow.com/new-york-ny/rentals/1-1_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22New%20York%2C%20NY%22%2C%22mapBounds%22%3A%7B%22west%22%3A-74.51765986914063%2C%22east%22%3A-73.43825313085938%2C%22south%22%3A40.39986454926866%2C%22north%22%3A41.010541890145014%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A6181%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A576423%2C%22max%22%3A1070499%7D%2C%22mp%22%3A%7B%22min%22%3A1400%2C%22max%22%3A2600%7D%2C%22beds%22%3A%7B%22min%22%3A1%2C%22max%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D",
    headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")
# print(soup.prettify())

all_link_elements = soup.select("#search-page-react-content ul li .list-card-info")
my_dict = {}
counter = 0
for element in all_link_elements:
    try:
        a = element.select_one(selector=".list-card-price").getText()
        b = element.select_one(selector="a").getText()
        c = element.select_one(selector="a")["href"]
        # print(a, b,c)
        my_dict[counter] = {
            "price": a,
            "location": b,
            "link": c
        }
        counter += 1
    except AttributeError:
        pass

print(my_dict)

FORMLINK = "https://docs.google.com/forms/d/e/1FAIpQLSd1U52yPKRBTKjNi_nGhC5kr_V1lfGoHGf8yddd2gf9SxeEEg/viewform?usp=sf_link"
driver.get(FORMLINK)
time.sleep(2)
for i in my_dict:
    price_form = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_form.send_keys(f"{my_dict[i]['price']}")

    location_form = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    location_form.send_keys(f"{my_dict[i]['location']}")

    link_form = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_form.send_keys(f"{my_dict[i]['link']}")
    time.sleep(1)
    button_click = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
    button_click.click()

    new_entry = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    new_entry.click()
driver.quit()




