from typing import *
import base64

def valid_url(url:str)->bool:
    # [TODO] implement valid url function to check url is valid or not
    '''
    Description: check url is valid or not
    params:
        url (str)
    return: str
    '''
    
    return True

def hashed_url(url: str)-> str:
    '''
    
    '''
    return base64.b64encode(url.encode('utf-8')).decode('utf-8')