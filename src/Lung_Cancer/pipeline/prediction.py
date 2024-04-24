import joblib
import numpy as np 
import pandas as pd
from pathlib import Path
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from Lung_Cancer.logging import logger



class PredictionPipeline():
    def __init__(self):
        self.model = joblib.load("/Users/melihaltin/Documents/Development/data-science/Lung-Cancer/Lung-Cancer/artifacts/model_training/model.joblib")
    
    
    def transform_data(self, data):
        logger.info("Transforming prediction data")
        
        encoder = LabelEncoder()
        data['GENDER'] = encoder.fit_transform(data['GENDER'])
                
        scaler=StandardScaler()
        data['AGE']=scaler.fit_transform(data[['AGE']])

        logger.info("Prediction Data transformed successfully")
        
        return data
    
    def predict(self, data):
        data = self.transform_data(data)
        prediction = self.model.predict(data)
        return prediction
        