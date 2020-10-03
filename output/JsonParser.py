import logging
from typing import Tuple

from output.JsonOutput import JsonOutput
from output.Parser import Parser


class JsonParser(Parser):

    def __init__(self, output: JsonOutput):
        super().__init__(output)
        self._logger = logging.getLogger(__name__)

    def get_cpu_sensor_temp(self, path: Tuple) -> float:
        value = self._output.get_data()
        out = value[path[0]][path[1]][path[2]]
        return float(out)

    def get_acip_sensor_temp(self, path: Tuple) -> float:
        value = self._output.get_data()
        out = value[path[0]][path[1]][path[2]]
        return float(out)

    def get_mvne_sensor_temp(self, path: Tuple) -> float:
        value = self._output.get_data()
        out = value[path[0]][path[1]][path[2]]
        return float(out)
