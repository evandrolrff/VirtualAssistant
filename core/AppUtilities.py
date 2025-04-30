from core.date.partial_date import PartialDate
from core.time.partial_time import PartialTime
from language import LanguageManager


class AppUtilities:

    @staticmethod
    def What_Should_Do(lg_manager: LanguageManager, response: str) -> str:
        print(response)
        if response == "time\getTime":
            return AppUtilities.__Get_Time(lg_manager)
        elif response == "time\getDate":
            return AppUtilities.__Get_Date(lg_manager)
        elif response == "time\getWeekday":
            return AppUtilities.__Get_Weekday(lg_manager)
        elif response == "weather\getWeather":
            return AppUtilities.__Get_Weather(lg_manager)
        else:
            return "Comando não reconhecido."


    @staticmethod
    def __Get_Time(lg_manager: LanguageManager) -> str:
        partial_time = PartialTime(lg_manager)
        return partial_time.get_time()


    @staticmethod
    def __Get_Date(lg_manager: LanguageManager) -> str:
        partial_date = PartialDate(lg_manager)
        return partial_date.get_date()


    @staticmethod
    def __Get_Weekday(lg_manager: LanguageManager) -> str:
        partial_date = PartialDate(lg_manager)
        return partial_date.get_day_of_week()



    @staticmethod
    def __Get_Weather(lg_manager: LanguageManager) -> str:
        return "Ensolarado"
