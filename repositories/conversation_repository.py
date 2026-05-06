from models.conversation import Conversation
from repositories.connection import get_connection

def get_conversations(limit: int = 10) -> list[Conversation]:
    sql = """ SELECT ROWID, chat_identifier, display_name FROM chat
            LIMIT ?
            """

    con = get_connection()
    cursor = con.execute(sql, (limit,))
    rows = cursor.fetchall()

    conversations_list = []
    for row_id, chat_identifier, display_name in rows:
        conversation = Conversation(
            id= row_id,
            chat_identifier=chat_identifier,
            display_name= display_name
        )
        conversations_list.append(conversation)

    return conversations_list