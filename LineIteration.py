class LineIteration():
    def __init__(self):
        self.current = 0
        self.__last_user_message_position = 0

    def get_last_user_message_position(self):
        return self.__last_user_message_position
        
    def mark_as_user_message(self):
        self.last_user_message_position = self.current
    