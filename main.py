import requests
from datetime import datetime as dt
import os

class Work_tracker:
    def __init__(self):
        APP_ID = os.environ['NU_APP_ID']
        APP_KEY = os.environ['NU_APP_KEY']
        AGE = 20
        HEIGHT = 167.64
        WEIGHT = 72.5
        GENDER = 'male'
        TODAY = dt.today().strftime('%d/%m/%Y')
        TIME = dt.now().strftime("%H:%M:%S")

        header = {
            'x-app-id': APP_ID,
            'x-app-key': APP_KEY,
        }

        user_input = input('Tell me which exercise you did today? ')
        url = 'https://trackapi.nutritionix.com/v2/natural/exercise'
        post_params = {
            "query": user_input,
            "gender": GENDER,
            "weight_kg": WEIGHT,
            "height_cm": HEIGHT,
            "age": AGE
        }
        response = requests.post(url=url, headers=header, json=post_params)
        result = response.json()

        shetty_post_url = ' https://api.sheety.co/bee3512ca4809c5fc6fb24f313e0dfad/workoutTrackerProject/workouts'
        shetty_header = {
            'Authorization': os.environ['SHETTY_AUTH_TOKEN']
        }
        for exercise in result["exercises"]:
            shetty_params = {
                'workout': {
                    'name': 'Ugochukwu Benjamin',
                    'email': 'kodiugos@gmail.com',
                    'date': TODAY,
                    'time': TIME,
                    'exercise': exercise['name'].title(),
                    'duration': exercise["duration_min"],
                    'calories': exercise["nf_calories"],
                }
            }
            shetty_response = requests.post(url=shetty_post_url, json=shetty_params, headers=shetty_header)
            print(shetty_response.text)


work_tracker = Work_tracker()
