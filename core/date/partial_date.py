import datetime
from datetime import date
from language import LanguageManager

class PartialDate():

    def __init__(self, lg_manager:LanguageManager) -> None:
        self.language_manager = lg_manager
        self.__weekday_map = {
            0: self.language_manager.get_message("monday"),
            1: self.language_manager.get_message("tuesday"),
            2: self.language_manager.get_message("wednesday"),
            3: self.language_manager.get_message("thursday"),
            4: self.language_manager.get_message("friday"),
            5: self.language_manager.get_message("saturday"),
            6: self.language_manager.get_message("sunday")
        }

    
    def get_date(self) -> str:
        now = datetime.date.today()
        answer = self.language_manager.get_message_with_fill_string("get_date", "{}/{}/{}".format(now.day, now.month, now.year))
        return answer
    
    
    def __get_weekday_name(self, input_date: date) -> str:
        """
        Retorna o nome do dia da semana para uma data fornecida.
        
        :param input_date: Instância de datetime.date
        :return: Nome do dia da semana (ex: "Monday")
        """
        weekday_number = input_date.weekday()
        return self.__weekday_map[weekday_number]

    
    def get_day_of_week(self) -> str:
        now = datetime.date.today()
        answer = self.language_manager.get_message_with_fill_string("get_day_of_week", "{}".format(self.__get_weekday_name(now)))
        return answer