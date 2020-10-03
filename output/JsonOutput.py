import json
import logging

from output.Output import Output


class JsonOutput(Output):

    def __init__(self, data):
        super().__init__(data)
        self._logger = logging.getLogger(__name__)
        self._decode()

    def print_row_data(self):
        print(str(self._data))

    def print_json(self):
        print(self._json)

    def log(self):
        self._logger.info(str(self._json))

    def _decode(self):
        self._json = json.loads(self._data)  # Decoding JSON

    def get_data(self):
        return self._json
