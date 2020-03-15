from io import open
import re as regex 
from LineIteration import * 
from Message import * 

class WhatsappChat (LineIteration):
    def __init__(self, filepath, encoding = "utf8"):
        self.__filepath = filepath
        self.__encoding = encoding
        self.__participants = []
        
    def format(self):
        self._get_lines()

    def _get_lines(self):
        chat = open(self.__filepath, encoding=self.__encoding)
        chat.seek(0)
        lines = chat.readlines()
        chat.close()
        lines = self.__line_process(lines)
        return lines

    def __line_process(self, lines):
        messages = []
        iteration = LineIteration()
        while(iteration.current < len(lines)):
            line = lines[iteration.current]
            message = Message(line)
            if message.has_remitter():
                iteration.mark_as_user_message()
                print("Mensaje de usuario")
            else:
                if message.has_creation_date():
                    print("Notificación")
                else:
                    print("Solo fue un salto de linea en el mensaje :) => ", line)
            iteration.current += 1
    
    def __add_participant_if_not_exist(self):
        print("oks")
    
    def isset(self, variable):
	    return variable in locals() or variable in globals()

WChat = WhatsappChat("./conversations/alex.txt")
lines = WChat.format()
