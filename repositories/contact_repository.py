from models.contact import Contact
from repositories.connection import get_connection

def get_contacts(limit: int = 10) -> list[Contact]:
    sql = """ SELECT ROWID, id, service FROM handle
            WHERE id IS NOT NULL
            LIMIT ?
            """

    con = get_connection()
    cursor = con.execute(sql, (limit,))
    rows = cursor.fetchall()

    contact_list = []
    for row_id, identifier, service in rows:
        contact = Contact(
            id= row_id,
            identifier= identifier,
            service= service
        )
        contact_list.append(contact)

    return contact_list