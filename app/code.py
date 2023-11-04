import requests
import numpy as np

animals = {0:"Dogs", 1:"Panda", 2:"Cats"}

# url = "http://localhost:8080/api/image/preprocessing"
url = "http://172.17.0.2:5000/api/image/preprocessing"

def callAPI(img, model):
    try:
        params = {"img_base64": img}

        response = requests.get(url, json=params)

        if response.status_code == 200:
            res = response.json()
            dataList = list(res.values())
            dataList = np.squeeze(dataList, axis=0)
            dataList = dataList.tolist()

            # ได้ค่าความน่าจะเป็นแต่ละคลาส
            animal_predict = model.predict(dataList)

            # เอา class ที่มีค่าความน่าจะเป็นสูงที่สุด
            animal_dict = np.argmax(animal_predict)

            # mapping ช่อง ดึงตำแหน่งที่ตรงกับ animals ออกมา
            animal = animals[animal_dict]
            
            return animal
        else:
            return {"error": f"API error number code : {response.status_code}"}
    except Exception as ex:
        return {"error": f" message: {str(ex)}"}