from pydantic import BaseModel

class Conversation(BaseModel):
    id: int 
    chat_identifier: str 
    display_name: str | None


    