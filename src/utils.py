import os
import sys
import pandas as pd
import numpy as no
import pickle
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from src.logger import logging
from src.exceptions import CustomException

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)

    except Exception as e:
        logging.info("Exception occured while saving the object")
        raise CustomException(e,sys)