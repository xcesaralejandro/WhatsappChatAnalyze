from io import open
import re as regex 
from LineIteration import * 
from Message import * 
import constant

class WhatsappChat (LineIteration):
    def __init__(self, filepath, encoding = "utf8"):
        self.__filepath = filepath
        self.__encoding = encoding
        self.__participants = []
        
    def format(self):
        self._get_lines()

    def _get_lines(self):
        lines = []
        try:
            chat = open(self.__filepath, encoding=self.__encoding)
            chat.seek(0)
            lines = chat.readlines()
            chat.close()
            lines = self.__line_process(lines)
        except FileNotFoundError:
            print("Chat file not found")
        return lines

    def __line_process(self, lines):
        messages = []
        iteration = LineIteration()
        while(iteration.current < len(lines)):
            line = lines[iteration.current]
            message = Message(line)
            if message.get("category") == constant.USER_MESSAGE:
                iteration.mark_as_user_message()
            iteration.current += 1
    
WChat = WhatsappChat("./conversations/alex.txt")
lines = WChat.format()
