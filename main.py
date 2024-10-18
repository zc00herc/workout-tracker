from datetime import datetime
import requests
import os


header = {
    'x-app-id': os.getenv('APP_ID'),
    'x-app-key': os.getenv('API_KEY'),
    'Authorization': os.getenv('SHEETY_TOKEN')
}



entry = input("Enter your workout: ")
exercise_parmeters = {
    'query': entry,
    # "weight": weight,
    # "height": height,
    # "age": age,
}

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

sheety_get_endpoint = 'https://api.sheety.co/7a68b96f49d65cd1d3b0ef4965b2ae87/workoutTracking/workouts'
sheety_post_endpoint = 'https://api.sheety.co/7a68b96f49d65cd1d3b0ef4965b2ae87/workoutTracking/workouts'

workout_response = requests.post(url=exercise_endpoint,headers=header,json=exercise_parmeters)
workout_response.raise_for_status()
returned_workout = workout_response.json()
print(returned_workout)

for index in range(0,len(returned_workout["exercises"])):
    data_to_add = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%y"),
            "time": datetime.now().strftime("%X"),
            "exercise": returned_workout["exercises"][index]["user_input"].title(),
            "duration": returned_workout["exercises"][index]["duration_min"],
            "calories": returned_workout["exercises"][index]["nf_calories"]
        }
    }

    sheety_response = requests.post(sheety_post_endpoint,json=data_to_add,headers=header)
    # sheety_response = requests.get(sheety_get_endpoint)
    sheety_response.raise_for_status()
    # print(sheety_response.text)
