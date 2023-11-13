import os
import sys

import numpy as np 
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

def save_object(file_path, obj):
    """
    The function `save_object` saves an object to a file using pickle, creating the necessary
    directories if they don't exist.
    
    :param file_path: The file path where the object will be saved. This should include the file name
    and extension
    :param obj: The `obj` parameter is the object that you want to save to a file. It can be any Python
    object that is serializable, meaning it can be converted into a byte stream and then reconstructed
    later. Examples of serializable objects include dictionaries, lists, strings, and custom classes
    that implement the
    """
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    


def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    """
    Evaluates the performance of different models using GridSearchCV and returns a dictionary of the test scores.

    Args:
        X_train (numpy.ndarray): Training data features.
        y_train (numpy.ndarray): Training data labels.
        X_test (numpy.ndarray): Test data features.
        y_test (numpy.ndarray): Test data labels.
        models (dict): Dictionary of models to be evaluated.
        param (dict): Dictionary of hyperparameters for each model.

    Returns:
        dict: A dictionary of the test scores for each model.
    """
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para = param[list(models.keys())[i]]

            gs = GridSearchCV(model, para, cv=3)
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)
    
def load_object(file_path):
    """
    The function `load_object` loads an object from a file using the `pickle` module in Python, and
    raises a `CustomException` if an error occurs.
    
    :param file_path: The file path is the location of the file that you want to load the object from.
    It should be a string that specifies the path to the file, including the file name and extension.
    For example, "C:/Users/username/Documents/my_object.pkl"
    :return: the object loaded from the file.
    """
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)