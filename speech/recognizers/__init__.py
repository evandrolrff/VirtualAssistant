from .google import GoogleMicrophone
from .vosk import VoskMicrophone

# Facilita o acesso aos reconhecedores:
__all__ = ["GoogleMicrophone", "VoskMicrophone"]
