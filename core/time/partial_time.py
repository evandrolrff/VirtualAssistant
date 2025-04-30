import datetime
from language import LanguageManager

class PartialTime():

    def __init__(self, lg_manager: LanguageManager):
        self.language_manager = lg_manager


    def get_time(self) -> str:
        now = datetime.datetime.now()
        answer = self.language_manager.get_message_with_fill_string("get_time", "{}:{}".format(now.hour, now.minute))
        return answer
    

