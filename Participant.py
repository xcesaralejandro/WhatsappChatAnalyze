from WeeklySummary import *
from datetime import datetime
import time
class Participant(WeeklySummary):
    def __init__(self, name):
        self.__name = name
        self.__weekly_summary = WeeklySummary()
        self.__last_recipient_message = None

    def reports(self):
        print("\n\n\n\n", self.__name)
        print("----------------------------------------------------")
        reports = {
            "general_summary" : self.__weekly_summary.general_summary()
        }
        return reports

    def is_owner(self, message):
        owner = self.__name == message['remitter']
        return owner

    def add_own_message(self, message):
        response_time = self.__get_response_time(message)
        self.__weekly_summary.add(message, response_time)

    def add_last_recipient_message(self, message):
        self.__last_recipient_message = message['created_at']
    
    def __get_response_time(self, message):
        response_time = None
        if self.__last_recipient_message:
            time_diference = self.__subtract_dates(self.__last_recipient_message, message['created_at'])
            if self.__valid_response_time(time_diference):
                response_time = time_diference
            self.__reset_last_recipient_message()
        return response_time
    
    def __valid_response_time(self, time_diference):
        valid = True
        if self.__last_message_in_sleep_time() and self.__sleep_range(time_diference): 
            valid = False
        return valid
    
    def __last_message_in_sleep_time(self):
        hour = datetime.strftime(self.__last_recipient_message, "%H")
        in_sleep_time = int(hour) in constant.SLEEP_HOURS
        return in_sleep_time

    def __sleep_range(self, minutes):
        sleeping = minutes >= constant.MIN_MINUTES_SLEEP and minutes <= constant.MAX_MINUTES_SLEEP
        return sleeping

    def __reset_last_recipient_message(self):
        self.__last_recipient_message = None

    def __subtract_dates(self, d1, d2):
        fmt = "%d-%m-%y %H:%M"
        d1_timestamp = time.mktime(d1.timetuple())
        d2_timestamp = time.mktime(d2.timetuple())
        result = int((d2_timestamp - d1_timestamp) / 60)
        return result
