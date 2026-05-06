from repositories.contact_repository import get_contacts as get_contacts_from_db
from models.contact import Contact

def get_contacts(limit:int = 10) -> list[Contact]:
    list_contacts = get_contacts_from_db(limit)
    return list_contacts