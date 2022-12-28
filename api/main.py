from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from router import func
from utils import get_org_url

app = FastAPI()
app.include_router(func.router, prefix="/api")


@app.get('/{url_hash}')
async def get_url(url_hash: str):
    url_obj = get_org_url(url_hash)
    if url_obj.error:
        return {
            "status": "failed",
            "reason": url_obj.reason
        }
    return RedirectResponse(url_obj.url)

@app.get('/health-check')
async def health_check():
    return {
        'live':True
    }