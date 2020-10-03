import logging
from abc import ABC, abstractmethod
from typing import Set, Tuple


class Output(ABC):
    def __init__(self, data):
        self._data: str = data

    @abstractmethod
    def print_row_data(self) -> str:
        pass

    @abstractmethod
    def log(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

