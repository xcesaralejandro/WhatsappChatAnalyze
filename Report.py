from WhatsappChat import * 

class Report(WhatsappChat):
    def __init__(self, filepath, encoding = "utf8"):
        super().__init__(filepath, encoding)
        print("PARTICIPANTES DE LA CONVERSACIÓN: ", super().get("participants"))