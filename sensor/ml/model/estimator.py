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
            x_transformed = self.preprocessor.trasform(x)
            y_pred = self.model.predict(x_transformed)
            return y_pred
        except Exception as e:
            raise e