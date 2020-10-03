import logging
from shell.Cmd import Cmd
from output.JsonOutput import JsonOutput
from output.JsonParser import JsonParser


class Config:
    CMD = "sensors -j"
    MQTT = {
        "url": "192.168.1.100",
        "port": 1883
    }
    CPU_SENSORS = ("coretemp-isa-0000", "Package id 0", "temp1_input")
    ACPI_SENSORS = ("acpitz-acpi-0", "temp1", "temp1_input")
    NVME_SENSORS = ("nvme-pci-0100", "Composite", "temp1_input")


def main():
    logging.basicConfig(filename='odroidn2temp.log', filemode='w',
                        format='%(asctime)s %(levelname)-8s %(name)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info("OdroidN2 Temp")

    cmd = Cmd(Config.CMD)
    cmd.run()
    json: JsonOutput = cmd.get_json_output()
    json.log()

    json_parser: JsonParser = JsonParser(json)
    logger.info(json_parser.get_cpu_sensor_temp(Config.CPU_SENSORS))
    logger.info(json_parser.get_acip_sensor_temp(Config.ACPI_SENSORS))
    logger.info(json_parser.get_mvne_sensor_temp(Config.NVME_SENSORS))


if __name__ == '__main__':
    main()
