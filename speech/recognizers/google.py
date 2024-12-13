from speech.interfaces import Creator
import speech_recognition as sr

class GoogleMicrophone(Creator):
    def __init__(self, lg_manager, microphone_index=None) -> None:
        """
        Inicializa o reconhecedor e configura o microfone.
        
        Args:
            lg_manager (obj): Gerenciador de idiomas.
            microphone_index (int): Índice do microfone, se houver múltiplos dispositivos.
        """
        super().__init__(lg_manager)
        self.recognition = sr.Recognizer()
        self.microphone = sr.Microphone(device_index=microphone_index)


    def start_recognition(self) -> None:
        running = True
        while running:
            try:
                # Captura de áudio
                with self.microphone as source:
                    print("Say something...")
                    audio = self.recognition.listen(source, timeout=5, phrase_time_limit=10)

                # Reconhecimento de fala
                text = self.recognition.recognize_google(audio)
                print(f"You said: {text}")

                # Respostas a comandos
                if "hello" in text.lower():
                    print("Hello! How can I assist you today?")
                elif "goodbye" in text.lower():
                    print("Goodbye! Have a great day.")
                    running = False  # Sai do loop
            except sr.UnknownValueError:
                print("I didn't understand that. Please try again.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
