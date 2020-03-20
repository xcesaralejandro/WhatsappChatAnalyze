from datetime import datetime
import json
import pprint

class WeeklySummary:
    def __init__(self):
        self.__week = self.__generate_week_days()

    def __generate_week_days(self):
        days = {
            "Mon" : { "hours" : self.__generate_hours() },
            "Tue" : { "hours" : self.__generate_hours() },
            "Wed" : { "hours" : self.__generate_hours() },
            "Thu" : { "hours" : self.__generate_hours() },
            "Fri" : { "hours" : self.__generate_hours() },
            "Sat" : { "hours" : self.__generate_hours() },
            "Sun" : { "hours" : self.__generate_hours() }
        }
        return days

    def __str__(self):
        return str(self.__week)
    
    def __generate_hours(self):
        hours = {}
        for hour in range(0,24):
            hours[hour] = {"count_messages" : 0 , "count_message_words" : 0, "response_times" : [] }
        return hours

    def add(self, message):
        created = message['created_at']
        day = self.__extract_from(created, "%a")
        hour = self.__extract_from(created, "%H")
        position = self.__week[day]['hours'][int(hour)]
        position['count_messages'] += 1
        position['count_message_words'] += message['information']['count_words']

    def __extract_from(self, date, extract):
        extracted = datetime.strftime(date, extract)
        return extracted