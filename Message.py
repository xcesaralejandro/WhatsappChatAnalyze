import re as regex 
import constant
from MessageSummary import *
from datetime import datetime
class Message(MessageSummary):
    def __init__(self, line):
        self.__raw_line = line
        self.__clear_raw_line()
        self.__remitter = self.__find_remitter()
        self.__created_at = self.__find_creation_date()
        self.__text = self.__find_text()
        self.__information = MessageSummary()
        self.__update_information()
    
    def __str__(self):
        return str(self.get())

    def get(self, field = None):
        values = {
            "remitter" : self.__remitter,
            "created_at" : self.__created_at,
            "text" : self.__text,
            "information" : self.__information.get(),
            "category" : self.__category()
        }
        if field:
            values = values[field]
        return values
    
    def add_text(self, text):
        text = self.__clean_text_message(text)
        self.__text = "{} {}".format(self.__text, text)
        self.__update_information()
        
    def __category(self):
        category = None
        if self.__has_remitter():
                category = constant.USER_MESSAGE
        else:
            if self.__has_creation_date():
                category = constant.SYSTEM_NOTIFICATION_MESSAGE
            else:
                category = constant.LINE_PREVIOUS_MESSAGE
        return category
    
    def __has_remitter(self):
        return self.__remitter
    
    def __has_creation_date(self):
        return self.__created_at

    def __clear_raw_line(self):
        self.__raw_line = self.__raw_line.replace("<Multimedia omitido>", "")

    def __find_remitter(self):
        match = regex.search(constant.USER_MESSAGE_REGEX, self.__raw_line)
        remitter = None
        if match: 
            match = match.string[match.start() : match.end()]
            remitter = self.__extract_name(match)
        return remitter
    
    def __extract_name(self, text):
        name = None
        splited = text.split("-")
        position = constant.FIRST_ELEMENT_AFTER_SPLIT_USER_MESSAGE
        while(position < len(splited)):
            fragment_text = splited[position]
            name = self.__clean_name(fragment_text)
            position += 1
        return name

    def __clean_name(self, text):
        text = text.replace(":","")
        text = text.strip()
        return text
    
    def __find_creation_date(self):
        match = regex.search(constant.CREATION_DATE_REGEX, self.__raw_line)
        creation_date = None
        if match: 
            match = match.string[match.start() : match.end()]
            creation_date = self.__extract_date(match)
        creation_date = self.__format_creation_date(creation_date)
        return creation_date
    
    def __format_creation_date(self, date):
        date = datetime.strptime(date,"%d-%m-%y %H:%M")
        return date

    def __extract_date(self, text):
        date = None
        splited = text.split(" - ")
        if splited:
            date = splited[0]
        return date 
    
    def __find_text(self):
        text = None
        if self.__category() == constant.USER_MESSAGE :
            text = self.__extract_text(constant.USER_MESSAGE)
        elif self.__category() == constant.SYSTEM_NOTIFICATION_MESSAGE:
            text = self.__extract_text(constant.SYSTEM_NOTIFICATION_MESSAGE)
        elif self.__category() == constant.LINE_PREVIOUS_MESSAGE:
            text = self.__clean_text_message(self.__raw_line)
        return text

    def __extract_text(self, category):
        text = None
        expression = None
        if category == constant.USER_MESSAGE:
            expression = constant.USER_MESSAGE_REGEX
        elif category == constant.SYSTEM_NOTIFICATION_MESSAGE: 
            expression = constant.CREATION_DATE_REGEX
        match = regex.search(expression, self.__raw_line)
        if match: 
            text = match.string[match.end() : len(match.string)]
            text = self.__clean_text_message(text)
        return text
    
    def __clean_text_message(self, text):
        text = text.replace("\n","")
        return text

    def __update_information(self):
        self.__information.count_words = len(self.__text.split())