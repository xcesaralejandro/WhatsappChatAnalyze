from datetime import datetime
import json
import pprint
import constant 

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
            hours[hour] = {"count_messages" : 0 , "count_multimedia" : 0, "count_message_words" : 0, "response_times" : [] }
        return hours

    def add(self, message, response_time = None):
        created = message['created_at']
        day = self.__extract_from(created, "%a")
        hour = self.__extract_from(created, "%H")
        self.__update_time_block(day, hour, message, response_time)

    def __update_time_block(self, day, hour, message, response_time):
        time_block = self.__week[day]['hours'][int(hour)]
        time_block['count_messages'] += 1
        if message.get("type") == constant.MULTIMEDIA_MESSAGE:
            time_block["count_multimedia"] += 1
        else:
            time_block['count_message_words'] += message['information']['count_words']
        if response_time or response_time == 0 :
            time_block['response_times'].append(response_time)

    def __extract_from(self, date, extract):
        extracted = datetime.strftime(date, extract)
        return extracted