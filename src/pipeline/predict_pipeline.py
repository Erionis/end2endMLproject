import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    """
    A class used to represent a pipeline for making predictions using a trained model and preprocessor.

    Attributes
    ----------
    None

    Methods
    -------
    predict(features):
        Predicts the target variable for the given features using the trained model and preprocessor.

    """
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl") 
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



import pandas as pd
import sys

class CustomData:
    """
    A class to represent custom data for prediction.

    ...

    Attributes
    ----------
    gender : str
        gender of the student
    race_ethnicity : str
        race/ethnicity of the student
    parental_level_of_education : str
        parental level of education of the student
    lunch : str
        type of lunch the student has
    test_preparation_course : str
        whether the student has completed a test preparation course or not
    reading_score : int
        reading score of the student
    writing_score : int
        writing score of the student

    Methods
    -------
    get_data_as_data_frame():
        Returns the custom data as a pandas DataFrame.
    """

    def __init__(  self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):

        self.gender = gender

        self.race_ethnicity = race_ethnicity

        self.parental_level_of_education = parental_level_of_education

        self.lunch = lunch

        self.test_preparation_course = test_preparation_course

        self.reading_score = reading_score

        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        """
        Returns the custom data as a pandas DataFrame.

        Returns
        -------
        pandas.DataFrame
            A DataFrame containing the custom data.
        """
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)