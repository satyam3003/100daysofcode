import requests
import smtplib
from bs4 import BeautifulSoup

header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}

url = "https://www.amazon.in/Redmi-Note-Moonlight-White-64GB/dp/B07XCXJN5W/ref=sr_1_3?dchild=1&keywords=redmi+note+7+pro&qid=1629439070&s=electronics&sr=1-3"

response = requests.get(url=url, headers=header)
# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
price = soup.find("span", {"id": "priceblock_ourprice"}).getText()
price_ints = price[1:].split(",")
final_price = float("".join(price_ints))
print(final_price)

if final_price > 15498:
    my_email = ''
    password = ''
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password='')
        connection.sendmail(from_addr=my_email,
                            to_addrs='baldawasatyam30@gmail.com',
                            msg=f'Subject:Buy Redmi note 7 pro \n\n buy Redmi note 7 pro at {final_price} in link {url}')  # Subject:--- to add subject ---- \n\n to indicate subject is over and further add content
