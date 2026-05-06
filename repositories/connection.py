import sqlite3
import os 

def get_connection():
    db_path = os.environ.get("IMESSAGE_DB_PATH", "~/Library/Messages/chat.db")
    expanded_db_path = os.path.expanduser(db_path)
    return sqlite3.connect(f"file:{expanded_db_path}?mode=ro", uri=True)
