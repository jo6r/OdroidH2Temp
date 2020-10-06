import logging
import subprocess
from output.JsonOutput import JsonOutput
from shell.OsSystem import OsSystem


class Cmd:
    fake_output = "output.json"

    def __init__(self, command):
        self._command: str = command
        self._logger = logging.getLogger(__name__)
        self._result: str = ""

    def run(self):
        self._logger.info("Run command: '{0}'".format(str(self._command)))
        if OsSystem.is_windows():
            self._result = self._read_fake_output()
        else:
            # output from process
            try:
                process = subprocess.Popen(self._command,
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE)
                stdout, stderr = process.communicate()
                self._result = stdout.decode('utf-8')
            except (subprocess.CalledProcessError, FileNotFoundError) as e:
                self._logger.critical("Exception during call process. {}".format(str(e)))

    def get_json_output(self) -> JsonOutput:
        return JsonOutput(self._result)

    def _read_fake_output(self) -> str:
        self._logger.warning("load fake output from file {}".format(self.fake_output))
        with open(self.fake_output) as f:
            res = f.read()
            return res
