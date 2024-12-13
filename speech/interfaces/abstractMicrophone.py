from __future__ import annotations
from abc import ABC, abstractmethod

from language import LanguageManager
from speech.TTS import TTS

class Creator(ABC):
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Microphone class. The Creator's subclasses usually provide the
    implementation of this method.
    """

    def __init__(self, lg_manager: LanguageManager) -> None:
        self.language_manager = lg_manager


    @abstractmethod
    def start_recognition(self) -> None:
        raise NotImplementedError("Este método deve ser implementado pela subclasse.")
    

    def assistant_speaking(self) -> None:
        raise NotImplementedError("Este método deve ser implementado pela subclasse.")
    
    
    def processes_speech_from_the_microphone(self) -> None:
        raise NotImplementedError("Este método deve ser implementado pela subclasse.")