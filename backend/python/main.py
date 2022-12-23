# TEST BACKEND IMPLEMENTATION
from http.client import HTTPException
from tracemalloc import start
from typing import Optional
from vital import Client
import json
# from fastapi import FastAPI
# from starlette.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
import os
# from dotenv import load_dotenv
# load_dotenv()

# app = FastAPI()
VITAL_API_KEY = os.getenv("VITAL_API_KEY")
VITAL_ENVIRONMENT = os.getenv("VITAL_ENV")
VITAL_REGION = os.getenv("VITAL_REGION")
VITAL_API_KEY = "sk_us_Up9SAgjbDo04pIySTH-eWcFCMq7b9TPwJGC1tolYrqU"
VITAL_ENVIRONMENT = "sandbox" #"sandbox" doesn't work?
VITAL_REGION = "us"

client = Client(api_key=VITAL_API_KEY, environment=VITAL_ENVIRONMENT, region=VITAL_REGION)
daniel_user_id = 'b1d28867-e695-4641-a2a4-9051a41ae752'
daniel = client.User.get(daniel_user_id)

daniel = client.User.resolve('43')
print(daniel.get("user_id"))
start_date = '2022-12-16 00:00:00'
end_date = '2022-12-16'
# sleep = client.Sleep.get(daniel_user_id, start_date, end_date)

# print(json.dumps(sleep, indent=4))
print('===============')
print('===============')
print('===============')
print('===============')
# print(sleep['sleep'][0]['awake'])
print('__________________________')
sleep = client.Sleep.get_stream_for_date_range(daniel_user_id, start_date, end_date)
sleep_thing = sleep['sleep'][0]['sleep_stream']['heartrate']
# print(json.dumps(sleep_thing, indent=4))
print(sleep_thing[0]['timestamp'])
#print(json.dumps(sleep, indent=4))
print('===============')
print('===============')
print('===============')
print('===============')
# print('__________________________')
# sleep = client.Sleep.get_raw(daniel_user_id, start_date, end_date)
# print(json.dumps(sleep, indent=4))
# day_count = 0
# print(sleep['sleep'][day_count]['data']['score'])
# print('===============')
# print('===============')
# print('===============')
# print('===============')
# print('===============')
# print('===============')
# print('===============')
# print('===============')
# print(sleep.get('sleep').get('data'))
# print('__________________________')
# print('__________________________')
# print('__________________________')
# sleep_list = sleep['sleep']
# for item in sleep_list[0]:
#     print(item)
#     print('===============')
#     print('===============')
#     print('===============')
#     print('===============')
























# app.add_middleware(  # type: ignore
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# @app.get("/token/{user_key}")
# def get_token(user_key: str):
#     return client.Link.create(user_key)


# class CreateUserData(BaseModel):
#     client_user_id: str


# @app.post("/user/")
# def create_user(data: CreateUserData):
#     return client.User.create(data.client_user_id)


# @app.get("/users/")
# def get_users():
#     return client.User.get_all()


# @app.get("/summary/{data_type}/{user_id}")
# def get_users(data_type: str, user_id: str, start_date: str, end_date: str):
#     func_map = {
#         "sleep": client.Sleep.get,
#         "activity": client.Activity.get,
#         "body": client.Body.get,
#         "workouts": client.Workouts.get,
#     }
#     func = func_map.get(data_type)
#     if not func:
#         raise HTTPException(400, "Failed to find data type")
#     data = func(user_id, start_date, end_date)
#     return data


# @app.get("/summary/{user_id}")
# def get_users(user_id: str, start_date: str, end_date: str):
#     sleep = client.Sleep.get(user_id, start_date, end_date)
#     activity = client.Activity.get(user_id, start_date, end_date)
#     body = client.Body.get(user_id, start_date, end_date)
#     workouts = client.Workouts.get(user_id, start_date, end_date)
#     return {"sleep": sleep, "activity": activity, "body": body, "workouts": workouts}
