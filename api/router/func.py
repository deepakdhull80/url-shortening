import os

from fastapi import APIRouter, Request

from model.main import RequestBase
from .utils import valid_url, hashed_url

router = APIRouter()

@router.post("/shorten")
async def create_shorten_url(body: RequestBase, request: Request):
    url = body.url

    if not valid_url(url):
        return {
            "url": url,
            "request": "Failed",
            "reason": "Not valid url found"
        }
    
    url_hash = hashed_url(url)

    #[TODO] store url_hash in db
    shorten_url = request.base_url.__str__() + url_hash

    return {
        "url": url,
        "request": "Completed",
        "result": shorten_url
    }
