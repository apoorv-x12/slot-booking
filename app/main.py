from fastapi import FastAPI
from app.db import execute
from app.services.booking import book_slot
from app.workers.analytics import run_analytics

app = FastAPI()

@app.post("/slots/{slot_id}/book")
async def book(slot_id: int):
    return await book_slot(execute, slot_id)

@app.get("/analytics")
def analytics():
    run_analytics()
    return {"status": "started"}
