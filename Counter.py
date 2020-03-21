class Counter:
    def __init__(self):
        self.__messages = 0
        self.__message_multimedia = 0
        self.__message_words = 0
        self.__response_times = []
    
    def __str__(self):
        values = {
            'messages': self.__messages,
            'message_multimedia': self.__message_multimedia,
            'message_words': self.__message_words,
            'response_times': self.__response_times,
        }
        return str(values)
    
    def get(self, field = None):
        values = {
            "messages" : self.__messages,
            "message_multimedia" : self.__message_multimedia,
            "message_words" : self.__message_words,
            "response_times" : self.__response_times,
        }
        if field:
            values = values[field]
        return values

    def count_message(self, value = 1):
        self.__messages += value

    def count_message_multimedia(self, value = 1):
        self.__message_multimedia += value
    
    def count__message_words(self, value = 1):
        self.__message_words += value
    
    def add__response_times(self, values):
        self.__response_times.extend(values)

    def add__response_time(self, value):
        self.__response_times.append(value)
    
    def _average(self, lst):
        average = 0 
        if len(lst) > 0:
            average = int(sum(lst) / len(lst)) 
        return average  
    