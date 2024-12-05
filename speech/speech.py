from speech.recognizers import GoogleMicrophone, VoskMicrophone

class SpeechRecognition:

    def __init__(self, model="vosk") -> None:
        if model == "vosk":
            self.speech_recognizer = VoskMicrophone()
        else:
            self.speech_recognizer = GoogleMicrophone()

        self.model = model

    def get_model(self) -> str:
        return self.model

    def initilize_recognition(self) -> None:
        self.speech_recognizer.start_recognition()