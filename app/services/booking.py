async def book_slot(db_execute, slot_id: int):
    result = await db_execute(
        """
        UPDATE slots
        SET status = 'BOOKED'
        WHERE id = :id AND status = 'FREE'
        """,
        {"id": slot_id}
    )

    if result.rowcount == 1:
        return {"status": "BOOKED"}
    return {"error": "Already booked"}
