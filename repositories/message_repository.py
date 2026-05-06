from models.message import Message
from repositories.connection import get_connection
from helpers.timestamps import normalize_timestamp

def get_recent_messages(limit: int = 10) -> list[Message]:
    sql_query = """SELECT m.ROWID, m.text, m.handle_id, m.date, m.is_from_me, m.cache_has_attachments
    FROM message m
    WHERE m.text IS NOT NULL
    ORDER BY m.date DESC
    LIMIT ?"""

    con = get_connection()
    cursor = con.execute(sql_query, (limit,))
    rows = cursor.fetchall()

    message_list = []
    for row_id, text, handle_id, date, is_from_me, has_attachments in rows:
        message = Message(
            id=row_id,
            text=text,
            handle_id=handle_id,
            date=normalize_timestamp(date),
            is_from_me=is_from_me,
            has_attachments=has_attachments
        )
        message_list.append(message)

    return message_list 


def search_messages(query:str, limit:int = 10) -> list[Message]:
    sql = """SELECT m.ROWID, m.text, m.handle_id, m.date, m.is_from_me, m.cache_has_attachments
            FROM message m
            WHERE m.text IS NOT NULL AND m.text LIKE ?

            ORDER BY m.date DESC
            LIMIT ?"""
    
    con = get_connection()
    cursor = con.execute(sql, (f"%{query}%", limit))
    rows = cursor.fetchall()

    message_list = []
    for row_id, text, handle_id, date, is_from_me, has_attachments in rows:
        message = Message(
            id=row_id,
            text=text,
            handle_id=handle_id,
            date=normalize_timestamp(date),
            is_from_me=is_from_me,
            has_attachments=has_attachments
        )
        message_list.append(message)

    return message_list 