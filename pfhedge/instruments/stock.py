from abc import ABC, abstractmethod

class Stock(ABC):

    def __init__(self):
        self._buffer = {}
    
    @abstractmethod
    def simulate(self):
        pass

    def register_buffer(self, name, tensor):
        self._buffer[name] = tensor

    @property
    def spot(self):
        name = "spot"

        if name not in self._buffer:
            raise ValueError("Simulate first")
        else:
            return self._buffer[name]
        



    