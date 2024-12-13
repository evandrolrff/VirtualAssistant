import pyttsx3

class TTS:
    def __init__(self, rate=150, volume=1.0) -> None:
        self.rate = rate
        self.volume = volume
        self.engine = None
        
        self._initilize_text_to_speech()

    def _initilize_text_to_speech(self) -> None:
        """Inicializa e seta algumas configurações do TTS"""
        try:
            self.engine = pyttsx3.init()
        except RuntimeError:
            print("\nFalha ao inicializar")
        except ImportError:
            print("\nDriver não encontrado")

        self.engine.setProperty('rate', self.rate)          # Velocidade
        self.engine.setProperty('volume', self.volume)      # Volume
        
        self._config_voice()

    def _config_voice(self, index=0) -> None:
        """Configura a voz veja documentação https://pyttsx3.readthedocs.io/en/latest/"""
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[index].id)  # depende de quantas opções o computador possui
    
    def text_to_speech(self, text: str) -> None:
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Erro durante a fala: {e}")