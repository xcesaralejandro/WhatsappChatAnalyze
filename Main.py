from io import open
import re as regex 
from Message import * 
import constant

class WhatsappChat ():
    def __init__(self, filepath, encoding = "utf8"):
        self.__filepath = filepath
        self.__encoding = encoding
        self.__messages = self.__get_messages()

    def __get_messages(self):
        messages = []
        try:
            chat = open(self.__filepath, encoding=self.__encoding)
            chat.seek(0)
            lines = chat.readlines()
            chat.close()
            messages = self.__line_process(lines)
        except FileNotFoundError:
            print("Chat file not found")
        return messages

    def __line_process(self, lines):
        messages = []
        iteration = 0
        while(iteration < len(lines)):
            line = lines[iteration]
            message = Message(line)
            if message.get("category") == constant.USER_MESSAGE:
                messages.append(message)
            elif message.get("category") == constant.LINE_PREVIOUS_MESSAGE:
                lastmessage = messages[len(messages) - 1]
                lastmessage.add_text(message.get("text"))
            iteration+=1
        print("MENSAJE 1: {} \n".format(messages[0].get("text")))
        print("MENSAJE 2: {}".format(messages[1].get("text")))

WChat = WhatsappChat("./conversations/alex.txt")
