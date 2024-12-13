from speech.recognizers import GoogleMicrophone, VoskMicrophone

class SpeechRecognition:
    def __init__(self, lg_manager, model="vosk") -> None:
        self.language_manager = lg_manager

        if model == "vosk":
            self.speech_recognizer = VoskMicrophone(lg_manager)
        else:
            self.speech_recognizer = GoogleMicrophone(lg_manager)

        self.model = model


    def get_model(self) -> str:
        return self.model


    def initilize_recognition(self) -> None:
        self.speech_recognizer.start_recognition()