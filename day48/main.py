from selenium import webdriver

chrome_developer_paths = "C:/Users/Satyam/Driver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_developer_paths)

url = "https://www.python.org/"

driver.get(url)

# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# search_bar = driver.find_element_by_id("twotabsearchtextbox")
# print(search_bar.get_attribute("value"))

# card = driver.find_element_by_css_selector(".cardmy h5")
# print(card.text)

dates = driver.find_elements_by_css_selector(".event-widget li time")
links = driver.find_elements_by_css_selector(".event-widget li a")
date_list = []
links_list = []

for link in links:
    links_list.append(link.text)

for date in dates:
    date_list.append(date.text)

my_dict = {i+1: {'time': date_list[i], 'name': links_list[i]} for i in range(len(date_list))}
print(my_dict)

# driver.close()      # closes the tab
driver.quit()  # closes the window
