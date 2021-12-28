import requests
from datetime import *

GENDER = "male"
WEIGHT_KG = 56
HEIGHT_CM = 157
AGE = 20

APP_ID = ""
API_KEY = ""
SHEET_TOKEN = "Bearer satyambaldawa3003"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

header_sheet = {
    "Authorization": SHEET_TOKEN
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

sheet_endpoint = "https://api.sheety.co/7a77507b38ce500e0a4bae3720bac8cc/myWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ").title()


parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=header_sheet)
    print(sheet_response.text)
