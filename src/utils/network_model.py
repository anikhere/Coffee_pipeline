from src.constants import *
class Network_model:
        def __init__(self,model,preprocessor):
            self.model= model
            self.preprocessor = preprocessor
        def predict(self,x):
            transformed = self.preprocessor.transform(x)
            predicted = self.model.predict(transformed)
            return predicted
