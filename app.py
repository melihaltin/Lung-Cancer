import numpy as np
from flask import Flask, request, render_template
import os 
from src.Lung_Cancer.pipeline.prediction import PredictionPipeline
import pandas as pd
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/train' , methods = ['GET'])
def train():
    os.system('python main.py')
    return "Model trained successfully"

@app.route('/predict', methods = ['POST' , 'GET'])
def predict():
    if request.method == 'POST':
        """
            GENDER: str
                AGE: int64
                SMOKING: int64
                YELLOW_FINGERS: int64
                ANXIETY: int64
                PEER_PRESSURE: int64
                CHRONIC DISEASE: int64
                FATIGUE : int64
                ALLERGY : int64
                WHEEZING: int64
                ALCOHOL CONSUMING: int64
                COUGHING: int64
                SHORTNESS OF BREATH: int64
                SWALLOWING DIFFICULTY: int64
                CHEST PAIN: int64
        """
        gender = str(request.form["GENDER"])
        age = int(request.form["AGE"])
        smoking = int(request.form["SMOKING"])
        yellow_fingers = int(request.form["YELLOW_FINGERS"])
        anxiety = int(request.form["ANXIETY"])
        peer_pressure = int(request.form["PEER_PRESSURE"])
        chronic_disease = int(request.form["CHRONIC DISEASE"])
        fatigue = int(request.form["FATIGUE"])
        allergy = int(request.form["ALLERGY"])
        wheezing = int(request.form["WHEEZING"])
        alcohol_consuming = int(request.form["ALCOHOL CONSUMING"])
        coughing = int(request.form["COUGHING"])
        shortness_of_breath = int(request.form["SHORTNESS OF BREATH"])
        swallowing_difficulty = int(request.form["SWALLOWING DIFFICULTY"])
        chest_pain = int(request.form["CHEST PAIN"])
        
        data = [gender , age , smoking , yellow_fingers , anxiety , peer_pressure , chronic_disease , fatigue , allergy , wheezing , alcohol_consuming , coughing , shortness_of_breath , swallowing_difficulty , chest_pain]
        columns = ["GENDER" , "AGE" , "SMOKING" , "YELLOW_FINGERS" , "ANXIETY" , "PEER_PRESSURE" , "CHRONIC DISEASE" , "FATIGUE " , "ALLERGY " , "WHEEZING" , "ALCOHOL CONSUMING" , "COUGHING" , "SHORTNESS OF BREATH" , "SWALLOWING DIFFICULTY" , "CHEST PAIN"]
        data = np.array(data).reshape(1 , -1)
        data = pd.DataFrame(data , columns = columns)
        
        prediction = PredictionPipeline().predict(data)
        
        if prediction[0] == 1:
            prediction = "You have lung cancer"
        else:
            prediction = "You don't have lung cancer"    
        
        return render_template('results.html' , prediction = str(prediction))
        

if __name__ == "__main__":
    app.run(host = "0.0.0.0" , port = 8080, debug = True)


