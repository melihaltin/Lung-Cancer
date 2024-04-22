from src.Lung_Cancer.logging import logger
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class DataTransformation:
    def __init__(self, config):
        self.config = config
        self.data = None

    def load_data(self):
        logger.info(f"Loading data from {self.config.data_file}")
        self.data = pd.read_csv(self.config.data_file)
        logger.info("Data loaded successfully")
        return self.data

    def transform_data(self):
        logger.info("Transforming data")
        self.data.drop_duplicates(inplace=True)
        
        

        encoder = LabelEncoder()
        self.data['LUNG_CANCER'] = encoder.fit_transform(self.data['LUNG_CANCER'])
        self.data['GENDER'] = encoder.fit_transform(self.data['GENDER'])
    
    
        X = self.data.drop(['LUNG_CANCER'],axis=1)
        y = self.data['LUNG_CANCER']
        
        
        smote = SMOTE()
        X_smote,y_smote = smote.fit_resample(X,y)
        X_train,X_test,y_train,y_test = train_test_split(X_smote,y_smote,random_state=42,stratify=y_smote)
        
        scaler=StandardScaler()
        X_train['AGE']=scaler.fit_transform(X_train[['AGE']])
        X_test['AGE']=scaler.transform(X_test[['AGE']])
        
        train = pd.concat([X_train,y_train],axis=1)
        test = pd.concat([X_test,y_test],axis=1)
        
        logger.info("Data transformed successfully")
        return train,test

    def save_data(self):
        logger.info(f"Saving data to {self.config.root_dir}")
        train , test = self.transform_data()
        train.to_csv(self.config.root_dir / "train.csv", index=False)
        test.to_csv(self.config.root_dir / "test.csv", index=False)
        logger.info("Data saved successfully")

    def run(self):
        self.load_data()
        self.transform_data()
        self.save_data()