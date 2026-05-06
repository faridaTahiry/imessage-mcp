from mcp.server.fastmcp import FastMCP
from services.message_service import get_recent_messages, search_messages, get_conversation
from services.formatters import format_message
from services.contact_service import get_contacts
from services.draft_service import draft_reply


mcp = FastMCP("iMessage")
@mcp.tool()
def imessage_get_recent(limit: int = 10) -> str: 
    """Returns the most recent iMessages, optionally limited by count."""

    list_messages = get_recent_messages(limit)
    formatted_messages = []
    for message in list_messages:
        formatted_messages.append(format_message(message))

    
    return "\n".join(formatted_messages)
    
@mcp.tool()
def imessage_search(query: str, limit:int = 10) ->str:
    """Returns iMessages containing query in text"""

    list_messages = search_messages(query,limit)
    formatted_messages = []
    for message in list_messages:
        formatted_messages.append(format_message(message))


    return "\n".join(formatted_messages)

@mcp.tool()
def imessage_list_contacts(limit:int = 10) ->str:
    """Returns list of contacts"""

    list_contacts = get_contacts(limit)
    formatted_contacts = []
    for contact in list_contacts:
        formatted_contacts.append(f"{contact.identifier} ({contact.service})")

    return "\n".join(formatted_contacts)

@mcp.tool()
def imessage_draft_reply(contact: str, context: str, intent: str) -> str:
    """Composes a draft reply to a contact based on conversation context and the user's intent."""

    prompt = draft_reply(contact,context,intent)
    return prompt 

@mcp.tool()
def imessage_get_conversation(contact:str, limit:int = 50) -> str:
    """Returns the most recent messages for a given contact"""

    list_messages = get_conversation(contact, limit)
    formatted_messages = []
    for message in list_messages:
        formatted_messages.append(format_message(message))

    return "\n".join(formatted_messages)

if __name__ == "__main__":
    mcp.run()