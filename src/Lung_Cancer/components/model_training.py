import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
import joblib

class ModelTrainer:
    def __init__(self, config):
        self.config = config
        self.model_training_config = config.get_model_training_config()
        self.train_data = self.model_training_config.train_data

    def train(self):
        train_df = pd.read_csv(self.train_data)
     
        X_train, y_train = train_df.drop('LUNG_CANCER', axis=1), train_df['LUNG_CANCER']
        
        
        model = RandomForestClassifier()
        model.fit(X_train, y_train)
        
        return model
    
    def save_model(self, model):
        model_path = self.model_training_config.root_dir / 'model.joblib'
        joblib.dump(model, model_path)
        
        return model_path
    