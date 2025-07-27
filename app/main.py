# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#      return {"message": "Welcome to the Uptime Logger Microservice!"}

import requests
# for step 4
from fastapi import FastAPI, BackgroundTasks
from typing import List

# for step 5 (do not use "from app import database" here, when uvicorn runs --app-dir app in Dockerfile, it will treat app/ as the root for import, so you just use "import database", not "from app import database")
import database

# for step 6
from database import SessionLocal, UptimeLog
from sqlalchemy.orm import Session
import datetime


app = FastAPI()

urls_to_monitor = [
    "https://example.com",
    "https://google.com"]


# DB session generator
# this function create and close the database session safely
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# uptime check function
def check_uptime(url: str):
    try:
        response = requests.get(url)
        return {"url": url, "status": response.status_code}
    except requests.exceptions.RequestException as e:
        return {"url": url, "status": "down", "error": str(e)}

# API endpoint to check uptime for all URL
@app.get("/check-uptime")
def check_all_urls():
    db = next(get_db())
    results = []       

    # Iterate over the URLs and check their uptime
    for url in urls_to_monitor:
        result = check_uptime(url)
        results.append(result)

        # Save the result to the database
        log = UptimeLog(
            url=result["url"],
            status=str(result["status"]),
            checked_at=datetime.datetime.utcnow()
        )
        db.add(log)

    db.commit()
    return {"results": results}
 
 

