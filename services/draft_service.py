def draft_reply(contact: str, context: str, intent: str) -> str:
    prompt = f"""
            Draft reply to {contact}:

            Context:
            {context}

            Intent: {intent}
            """
    
    return prompt
