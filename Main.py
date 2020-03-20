from WhatsappChat import * 

wchat = WhatsappChat("./conversations/alex.txt")
messages = wchat.get("messages")
participants = wchat.get("participants")

for message in messages:
    message = message.get()
    for name in participants.keys():
        participant = participants[name]
        if participant.is_owner(message):
            participant.add_own_message(message)
        else:
            participant.add_last_recipient_message(message)

