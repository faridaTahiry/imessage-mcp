from models.message import Message

def format_message(message: Message) -> str:

    from_person = "Me" if message.is_from_me else "Them"
    formatted_message = f"[{message.date.strftime("%Y-%m-%d %H:%M")}] {from_person}: {message.text}"

    return formatted_message