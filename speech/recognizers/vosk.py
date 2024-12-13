from speech.interfaces import Creator
from vosk import Model, KaldiRecognizer
import sounddevice as sd
import queue
import sys
import os


class VoskMicrophone(Creator):
    def __init__(self, lg_manager, model_path="model", samplerate=None, blocksize=8000):
        """
        Inicializa a classe SpeechVosk.

        Args:
            lg_manager (obj): Gerenciador de idiomas.
            model_path (str): Caminho para a pasta do modelo Vosk.
            samplerate (int): Taxa de amostragem do microfone. Se None, será detectada automaticamente.
            blocksize (int): Tamanho dos blocos de áudio capturados.
        """
        super().__init__(lg_manager)
        self.model_path = os.path.join(os.path.dirname(__file__), "model")

        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Diretório do modelo não encontrado: {self.model_path}")
        
        self.samplerate = samplerate
        self.blocksize = blocksize
        self.q = queue.Queue()
        self.model = None
        self.recognizer = None

        self._initialize_model()
        self._initialize_audio_settings()


    def _initialize_model(self) -> None:
        """Carrega o modelo Vosk."""
        try:
            self.model = Model(self.model_path)
        except Exception as e:
            raise RuntimeError(f"Erro ao carregar o modelo Vosk: {e}")


    def _initialize_audio_settings(self) -> None:
        """Configura o microfone e obtém a taxa de amostragem padrão."""
        try:
            device_info = sd.query_devices(None, "input")
            if self.samplerate is None:
                self.samplerate = int(device_info["default_samplerate"])
        except Exception as e:
            raise RuntimeError(f"Erro ao configurar o dispositivo de áudio: {e}")


    def _callback(self, indata, frames, time, status) -> None:
        """Callback chamado para capturar o áudio."""
        if status:
            print(status, file=sys.stderr)
        self.q.put(bytes(indata))


    def start_recognition(self) -> None:
        """Inicia o reconhecimento de fala em tempo real."""
        try:
            with sd.RawInputStream(samplerate=self.samplerate, blocksize=self.blocksize,
                                   device=None, dtype="int16", channels=1, callback=self._callback):
                print("#" * 80)
                print("Capturando áudio. Pressione Ctrl+C para parar.")
                print("#" * 80)

                self.recognizer = KaldiRecognizer(self.model, self.samplerate)
                while True:
                    data = self.q.get()
                    if self.recognizer.AcceptWaveform(data):
                        result = self.recognizer.Result()
                    else:
                        result = self.recognizer.PartialResult()

                    # Processar resultado e exibir se válido
                    if result:
                        text = eval(result).get("text", "").strip()
                        if text:
                            print(f"Transcrição: {text}")
        except KeyboardInterrupt:
            print("\nCaptura encerrada.")
        except Exception as e:
            print(f"Erro durante o reconhecimento: {e}")