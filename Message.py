import re as regex 

class Message():
    def __init__(self, line):
        self.__raw_line = line
        self.__remitter = self.find_remitter()
        self.__creation_date = self.find_creation_date()
    
    def has_remitter(self):
        return self.__remitter
    
    def has_creation_date(self):
        return self.__creation_date

    def find_remitter(self):
        has_remitter = regex.search("\d{2}-\d{2}-\d{2} \d{2}:\d{2} -.{1,}:", self.__raw_line)
        return has_remitter
    
    def find_creation_date(self):
        has_creation_date = regex.search("\d{2}-\d{2}-\d{2} \d{2}:\d{2} -", self.__raw_line)
        return has_creation_date
