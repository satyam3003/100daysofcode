# ---------------- Using API --------------------
import requests
import datetime
import time as tim
import smtplib

# ----------------- my Lat, long --------------------
MY_LAT = 20.5937
MY_LNG = 78.9629

# --------------- Emain and password -------------------
MY_EMAIL = 'satyam30032001@gmail.com'
MY_PASSWORD = 'Baldawa@30'


# --------------- Get hour from time in sunrise and sunset --------------
def get_hr(time):
    hr = time.split('T')[1]
    hour = hr[0:2]
    return int(hour)


# ---------------- Parameters for sunrise&set api --------------------------
parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0,
    'date': 'today',
}


def dark():
    # ----------------- Current time in hrs -------------------
    now = datetime.datetime.now()
    current_hour = int(now.hour)
    print(f"current_hour: {current_hour}")

    # ------------------ Sunrise and sunset API -----------------
    b = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    b.raise_for_status()
    sunrise_data = b.json()
    sunrise = sunrise_data['results']['sunrise']
    sunrise = get_hr(sunrise)
    sunset = sunrise_data['results']['sunset']
    sunset = get_hr(sunset)
    print(f"sunset: {sunset} ,\tsunrise: {sunrise} ")
    # ------------------ Check if its dark --------------------
    if sunset < current_hour or current_hour < sunrise:
        print('its dark')
        return True
    else:
        return False


def near_my_location():
    # ----------------- Current location of space station --------------
    a = requests.get(url='http://api.open-notify.org/iss-now.json')  # saving the response in a
    a.raise_for_status()  # checking if the request was successful
    data = a.json()  # obtaining json data from a
    # print(data)    # The data is a normal dict
    long = data['iss_position']['longitude']
    lat = data['iss_position']['latitude']
    iss_position = (float(lat), float(long))
    print(f"current location of space station: {iss_position}\nmy location: {(MY_LAT, MY_LNG)}")

    # ------------------- difference between sat pos and my location --------------
    lat_dif = abs(MY_LAT - iss_position[0])
    lng_dif = abs(MY_LNG - iss_position[1])
    print(f"Lat dif: {lat_dif}\tLng dif: {lng_dif}")
    if lat_dif <= 5 and lng_dif <= 5:
        return True
    else:
        return False


def send_email():
    connection = smtplib.SMTP('smtp.gmail.com')
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs='baldawasatyam30@gmail.com',
                        msg='Subject:Look up\n\n International space station is above...!!!')


while True:
    if dark():
        # ----------------- Check is Space station is near my location -----------------
        if near_my_location():
            print('look up')
            send_email()
            tim.sleep(500)
    tim.sleep(60)
