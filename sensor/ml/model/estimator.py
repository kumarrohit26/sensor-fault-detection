from sensor.constant.training_pipeline import SAVED_MODEL_DIR, MODEL_FILE_NAME
import os
class TargetValueMapping:
    def __init__(self):
        self.neg: int = 0
        self.pos: int = 1

    def to_dict(self):
        return self.__dict__
    
    def reverse_mapping(self):
        mapping_response = self.to_dict()
        return dict(zip(mapping_response.values(), mapping_response.keys()))
    

# write code to train model and check accuracy

class SensorModel:

    def __init__(self, preprocessor, model):
        try:
            self.preprocessor = preprocessor
            self.model = model
        except Exception as e:
            raise e
        
    def predict(self, x):
        try:
            x_transformed = self.preprocessor.transform(x)
            y_pred = self.model.predict(x_transformed)
            return y_pred
        except Exception as e:
            raise e
        
class ModelResolver:

    def __init__(self, model_dir = SAVED_MODEL_DIR):
        try:
            self.model_dir = model_dir
        except Exception as e:
            raise e
        
    def get_best_model_path(self) -> str:
        try:
            timestamps = list(map(int, os.listdir(self.model_dir)))
            latest_timestamp = max(timestamps)
            print('latest timestamp ', latest_timestamp)
            latest_model_path = os.path.join(self.model_dir, f'{latest_timestamp}', MODEL_FILE_NAME)
            return latest_model_path
        except Exception as e:
            raise e
    
    def is_model_exists(self) -> bool:
        try:
            if not os.path.exists(self.model_dir):
                return False
            
            timestamps = os.listdir(self.model_dir)
            if len(timestamps) == 0:
                return False
            
            latest_model_path = self.get_best_model_path()

            if not os.path.exists(latest_model_path):
                return False
            
            return True
        except Exception as e:
            raise e