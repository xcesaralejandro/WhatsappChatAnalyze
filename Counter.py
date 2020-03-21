import pprint
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
    
    def summary(self):
        print("\n\nTotal de mensajes enviados",self.__messages)
        print("\nPromedio de palabras por mensaje",self.__average_words_per_message())
        print("\nTiempo promedio de respuesta (Minutos)",self.__average_from_list(self.__response_times))
        print("\nTotal de palabras escritas en la conversación",self.__message_words)
        print("\nTotal de mensajes multimedia enviados(stickers, adjuntos)",self.__message_multimedia)
        summary = { 
            "Total de mensajes enviados" : self.__messages,
            "Total de mensajes multimedia enviados(stickers, adjuntos)" : self.__message_multimedia,
            "Total de palabras escritas en la conversación" : self.__message_words,
            "Tiempo promedio de respuesta (Minutos)" : self.__average_from_list(self.__response_times),
            "Promedio de palabras por mensaje" : self.__average_words_per_message(),
        }
        # pprint.pprint(summary)
        return summary

    def __average_words_per_message(self):
        average = 0
        messages = self.__messages - self.__message_multimedia
        if messages > 0:
            average = int(self.__message_words / messages)
        return average

    def __average_from_list(self, lst):
        average = 0 
        if len(lst) > 0:
            average = int(sum(lst) / len(lst)) 
        return average  
    