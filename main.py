from speech import SpeechRecognition

if __name__ == "__main__":
    print("Welcome! I'm Alfred your assistant virtual!")
    
    recognizer = SpeechRecognition()
    print(f"I will utilize the model {recognizer.get_model()}")

    recognizer.initilize_recognition()
    