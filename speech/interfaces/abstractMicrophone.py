from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC):
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Microphone class. The Creator's subclasses usually provide the
    implementation of this method.
    """

    @abstractmethod
    def start_recognition(self) -> None:
        """
        Note that the Creator may also provide some default implementation of
        the factory method.
        """
        raise NotImplementedError("Este método deve ser implementado pela subclasse.")