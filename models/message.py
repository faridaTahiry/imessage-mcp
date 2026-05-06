from pydantic import BaseModel
from datetime import datetime

class Message(BaseModel):
    id: int
    text: str | None 
    handle_id: int 
    date: datetime
    is_from_me: bool 
    has_attachments: bool 