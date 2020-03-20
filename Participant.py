from WeeklySummary import *

class Participant(WeeklySummary):
    def __init__(self, name):
        self.__name = name
        self.__general_response_times = []
        self.__general_words_per_message = []
        self.__weekly_summary = WeeklySummary()
        self.__last_recipient_message = None

    def __str__(self):
        values = {
            "name" : self.__name,
            "weekly_summary" : self.__weekly_summary
        }
        return str(values)

    def is_owner(self, message):
        owner = self.__name == message['remitter']
        return owner

    def add_own_message(self, message):
        # if self.__last_recipient_message:
        #     pass
        # else:
        #     print("Primer mensaje", message)
        self.__weekly_summary.add(message)

    def add_last_recipient_message(self, message):
        self.__last_recipient_message = message['created_at']
