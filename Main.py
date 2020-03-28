from WhatsappChat import * 
import pprint
import io

filename = input("Nombre del fichero:")

wchat = WhatsappChat("./conversations/{}.txt".format(filename))
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

for name in participants.keys():
        participant = participants[name]
        participant.reports()

