class MessageSummary():
    def __init__(self):
        self.count_words = 0
    
    def __str__(self):
        return str(self.get())

    def get(self, field = None):
        values = {
            "count_words" : self.count_words,
        }
        if field:
            values = values[field]
        return values