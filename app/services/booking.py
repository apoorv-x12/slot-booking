
async def book_slot(db_exec, slot_id: int):
    result = await db_exec(
        """
        UPDATE slot_booking_status
        SET status = 'BOOKED'
        WHERE id = :id AND status = 'FREE'
        """,
        {"id": slot_id}
    )
    
    
    if result.rowcount == 1:
        return {"status": "BOOKED"}
    else:
        return {"error": "Already booked"}