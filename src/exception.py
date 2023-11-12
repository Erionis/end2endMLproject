import sys
from src.logger import logging

def error_message_detail(error,error_detail):
    '''
    this function will return the error message with the file name and line number
    '''
    _,_,exc_tb=error_detail.exc_info()
    filename=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] with error message [{2}]".format(filename,exc_tb.tb_lineno,str(error))
    
    return error_message
    
class CustomException(Exception):
    '''
    This is the custom exception class which will be used to raise the exception
    '''
    def __init__(self,error_meassage,error_detail:sys):
        super().__init__(error_meassage)
        self.error_message=error_message_detail(error_meassage,error_detail=error_detail)
        
    def __str__(self):
        return self.error_message

