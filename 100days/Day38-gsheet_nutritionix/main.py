import os

import requests
import datetime as dt


GMAIL_USED = os.environ["GMAIL_USED"]
NUTRI_APP_ID = os.environ["NUTRI_APP_ID"]
NUTRI_API_KEY = os.environ["NUTRI_API_KEY"]
SHEETY_AUTHZ = os.environ["SHEETY_AUTHZ"]
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]

header = {
    "x-app-id" : NUTRI_APP_ID,
    "x-app-key" : NUTRI_API_KEY,
}

url_base_exercise =  "https://trackapi.nutritionix.com"
endpoint_exercise = "v2/natural/exercise"

exercise_ask = input("Which exercise you did? ")
exercise_params = {
    "query" : exercise_ask
}
# yoga 30 mins, run 10 min
exercise_response = requests.post(url=f"{url_base_exercise}/{endpoint_exercise}", json=exercise_params, headers=header)
# print(exercise_response.status_code)
# print(exercise_response.text)
exercise_dict = exercise_response.json()


sheety_url = SHEETY_ENDPOINT

time = dt.datetime.now()
today, time_now = time.strftime("%d/%m/%Y"), time.strftime("%X")
# print(today, time_now, type(today), type(time_now)) # TEST

sheety_header = {
    "Content-Type" : "application/json",
    "Authorization": SHEETY_AUTHZ,
}

for exercise in exercise_dict["exercises"]:
    params = {
        "workout" :
        {"date" : today,
        "time" : time_now,
        "exercise": exercise["name"].title(),
        "duration" : exercise["duration_min"],
        "calories" : exercise["nf_calories"]
         }
    }



    sheety_upload = requests.post(url=sheety_url, json=params, headers=sheety_header)
    # print(sheety_upload.status_code)
