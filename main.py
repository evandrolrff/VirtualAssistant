from speech import SpeechRecognition
from language import LanguageManager

if __name__ == "__main__":
    lang_manager = LanguageManager(default_language="pt")

    print(lang_manager.get_message("greeting"))
    
    recognizer = SpeechRecognition(lg_manager=lang_manager)
    print(lang_manager.get_message_with_fill_string("model_utilized", recognizer.get_model()))

    recognizer.initilize_recognition()
    