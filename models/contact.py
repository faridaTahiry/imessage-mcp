from pydantic import BaseModel

class Contact(BaseModel):
    id: int 
    identifier: str 
    service: str 


    