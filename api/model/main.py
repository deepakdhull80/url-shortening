from typing import *

from pydantic import BaseModel

class RequestBase(BaseModel):
    url: str
