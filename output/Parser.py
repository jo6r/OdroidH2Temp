from abc import ABC, abstractmethod
from typing import Tuple

from output.Output import Output


class Parser(ABC):
    def __init__(self, output: Output):
        self._output: Output = output

    @abstractmethod
    def get_cpu_sensor_temp(self, path: Tuple) -> float:
        pass

    @abstractmethod
    def get_acip_sensor_temp(self, path: Tuple) -> float:
        pass

    @abstractmethod
    def get_mvne_sensor_temp(self, path: Tuple) -> float:
        pass