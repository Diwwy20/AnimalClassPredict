from fastapi import FastAPI, Request
from app.code import callAPI
# from code import callAPI
import os
import tensorflow as tf
from tensorflow import keras
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# print(os.getcwd() + "/model/animals_model.h5")
# model = keras.models.load_model("../model/animals_model.h5")
model = keras.models.load_model(os.getcwd() + "/model/animals_model.h5")


@app.get("/")
def root():
    return {"message": "This is my api"}

@app.post("/api/predict/animal")
async def read_str(data: Request):
    json = await data.json()
    image_str = json['img_base64']
    animal = callAPI(image_str, model)

    return {"Animal": animal}