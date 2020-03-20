from io import open
from Message import * 
from Participant import *
import constant

class WhatsappChat ():
    def __init__(self, filepath, encoding="utf8"):
        self.__filepath = filepath
        self.__encoding = encoding
        self.__messages = []
        self.__participants = []
        self.__process_file()

    def __str__(self):
        return str(self.get())
        
    def get(self, field = None):
        values = {
            "filepath" : self.__filepath,
            "encoding" : self.__encoding,
            "messages" : self.__messages,
            "participants" : self.__get_participants(),
        }
        if field:
            values = values[field]
        return values

    def __get_participants(self):
        all = {}
        for participant in self.__participants:
            all[participant] = Participant(participant)
        return all

    def __process_file(self):
        messages = []
        try:
            chat = open(self.__filepath, encoding=self.__encoding)
            chat.seek(0)
            lines = chat.readlines()
            chat.close()
            messages = self.__lines_process(lines)
        except FileNotFoundError:
            print("Chat file not found")
        self.__messages = messages

    def __lines_process(self, lines):
        messages = []
        iteration = 0
        while(iteration < len(lines)):
            line = lines[iteration]
            message = Message(line)
            if message.get("category") == constant.USER_MESSAGE:
                self.__add_participant(message.get("remitter"))
                messages.append(message)
            elif message.get("category") == constant.LINE_PREVIOUS_MESSAGE:
                lastmessage = messages[len(messages) - 1]
                lastmessage.add_text(message.get("text"))
            iteration+=1
        return tuple(messages)
    
    def __add_participant(self, name):
        if name and name not in self.__participants:
            self.__participants.append(name)
