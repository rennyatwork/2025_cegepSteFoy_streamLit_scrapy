from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess

app = FastAPI()

class ScrapeRequest(BaseModel):
    url: str

@app.post("/scrape")
async def scrape(request: ScrapeRequest):
    try:
        url = request.url
        # Run the Scrapy spider (Scrapy will handle the scraping)
        subprocess.run(["scrapy", "crawl", "simple_spider", "-a", f"url={url}"])
        return {"message": "Scraping completed"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
