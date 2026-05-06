from models.message import Message
from repositories.message_repository import get_recent_messages as get_recent_messages_from_db
from repositories.message_repository import search_messages as search_message_in_db, get_conversation as get_conversation_from_db

def get_recent_messages(limit: int = 10) -> list[Message]:
    list_messages = get_recent_messages_from_db(limit)
    return list_messages

def search_messages(query: str, limit: int = 10) -> list[Message]:
    list_messages = search_message_in_db(query,limit)
    return list_messages

def get_conversation(contact: str, limit: int = 50) -> list[Message]:
    list_messages = get_conversation_from_db(contact,limit)
    return list_messages