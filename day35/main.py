import requests
import os
from twilio.rest import Client

# MY_LON = 73.8553
# MY_LAT = 18.5196
# +16194942596
MY_LON = 75
MY_LAT = 26
api_key = '7000cfce40e060f640e863a505bd8330'

parameters = {
    'lat': MY_LAT,
    'lon': MY_LON,
    'exclude': 'current,minutely,daily',
    'appid': api_key,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
hourly_data = data['hourly'][:12]
hourly_weather_list = [item['weather'][0]['id'] for item in hourly_data if item['weather'][0]['id'] < 700]
if len(hourly_weather_list) > 0:
    send_message = 'Bring an umbrella today ☂'
else:
    send_message = 'Its a beautiful day 🌞'

# Download the helper library from https://www.twilio.com/docs/python/install
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC229886e1b6d27258f49a032d5d1a99fa'
auth_token = '03a12a7328890f7a3274fbc059d04f85'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
        body=send_message,
        from_='+16194942596',
        to='+918983517226'
    )
print(message.status)
