from typing import *
import base64

class Url:
    def __init__(self, url, error = False) -> None:
        self.error = error
        self.url = url
        self.reason = None
    
    def __str__(self) -> str:
        return f"URL(url='{self.url}', error='{self.error}', reason='{self.reason}')"

def get_org_url(url_hash: str)-> Url:
    '''
    params:
        url_hash (str): hash value
    return Url
    '''
    org_url = base64.b64decode(url_hash).decode('utf-8')
    return Url(
        url=org_url
    )