from cloudpickle import load
from typing import List
from datetime import datetime
from sklearn.datasets import load_iris
from sklearn.datasets import load_breast_cancer
import numpy as np

import warnings
warnings.filterwarnings('ignore')

import os
import numpy as np

class ClassifierModel(mlrun.runtimes.MLModelServer):
    def load(self):
        """Load model from storage."""
        model_file, extra_data = self.get_model('.pkl')
        self.model = load(open(model_file, 'rb'))

    def predict(self, body: dict) -> List:
        """Generate model predictions from sample.
        
        :param body : A dict of observations, each of which is an 1-dimensional feature vector.
            
        Returns model predictions as a `List`, one for each row in the `body` input `List`.
        """
        try:
            feats = np.asarray(body['instances'])
            result: np.ndarray = self.model.predict(feats)
            resp = result.tolist()
        except Exception as e:
            raise Exception(f"Failed to predict {e}")
        
        return resp
    

sample = [[1.371e+01, 2.083e+01, 9.020e+01, 5.779e+02, 1.189e-01, 1.645e-01,
           9.366e-02, 5.985e-02, 2.196e-01, 7.451e-02, 5.835e-01, 1.377e+00,
           3.856e+00, 5.096e+01, 8.805e-03, 3.029e-02, 2.488e-02, 1.448e-02,
           1.486e-02, 5.412e-03, 1.706e+01, 2.814e+01, 1.106e+02, 8.970e+02,
           1.654e-01, 3.682e-01, 2.678e-01, 1.556e-01, 3.196e-01, 1.151e-01],
          [20.57, 17.77, 132.9, 1326.0, 0.08474, 0.07864, 0.0869, 0.07017, 0.1812,
           0.05667, 0.5435, 0.7339, 3.398, 74.08, 0.005225, 0.01308, 0.0186, 0.0134,
           0.01389, 0.003532, 24.99, 23.41, 158.8, 1956.0, 0.1238, 0.1866, 0.2416,
           0.186, 0.275, 0.08902]]

my_server = ClassifierModel('classifier', model_dir=model)
my_server.load()

my_server.predict({"instances": sample})