from fastapi import FastAPI
from db import execute
from services.booking import book_slot

app= FastAPI()

@app.post("/slot/{slot_id}/book")
async def root(slot_id: int):
     
    result = await book_slot(execute, slot_id)
    return result
    