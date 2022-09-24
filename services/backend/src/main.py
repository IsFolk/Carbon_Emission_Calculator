import json
from fastapi import FastAPI, Request
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware  # NEW
from starlette.middleware import Middleware
import joblib
from os.path import dirname, join, realpath
from typing import List

#處理request的IP位址及允許header型態
middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['http://127.0.0.1'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )
]

app = FastAPI(middleware=middleware)


class TextArea(BaseModel):
    content: str
    
class Item(BaseModel):
    name: str
    description: str
    
#測試用router
@app.post("/add")
async def post_textarea(data:TextArea):
    print(data.content)
    return data


# load  model
with open(
    join(dirname(realpath(__file__)), "models/IrisClassifier.pkl"), "rb"
) as f:
    model = joblib.load(f)

# 整理進來的data格式
def data_clean(str):
    arr = str.split(',')
    arr = list(map(float,arr))
    return arr


# Create Prediction Endpoint
# 若URL收到predict-result的post需求則跑下方程式碼
@app.post("/predict-result")
async def predict_iris(request:TextArea):
    # perform prediction
    
    #先看一下request傳過來的型式
    print(json.loads(request.content))
    
    #data格式
    predata = json.loads(request.content)
    
    #model input feature
    arr = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    aftdata = {}
    
    #處理data
    for each in predata:
        if each["name"] in arr:
            aftdata[each["name"]] = each["value"]  
    data_for_predict = []
    for feature in arr:
        if feature in aftdata.keys():
            data_for_predict.append(aftdata[feature])
            
            
    print(data_for_predict)
    request = data_for_predict
    #處理字符型態
    request = list(map(float, request))

    #進行預測
    prediction = model.predict([request])
    output = int(prediction[0])
    probas = model.predict_proba([request])
    output_probability = "{:.2f}".format(float(probas[:, output]))
    
    # output dictionary
    species = {0: "Setosa", 1: "Versicolour", 2:"Virginica"}
    
    # show results
    result = {"prediction": species[output], "Probability": output_probability}
    print(result)
    

    return result

#測試用router get形式
@app.get("/")
async def serve_home(request: Request):
    return "Hello, World!"
    # return templates.TemplateResponse("index.html", {"request": request})