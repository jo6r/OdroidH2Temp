import logging
import json
from mqtt.MqttClient import MqttClient
from shell.Cmd import Cmd
from output.JsonOutput import JsonOutput
from output.JsonParser import JsonParser


class Config:
    CMD = ['sensors', '-j']
    MQTT = {
        "url": "192.168.1.100",
        "port": 1883
    }
    CPU_SENSORS = ("coretemp-isa-0000", "Package id 0", "temp1_input")
    ACPI_SENSORS = ("acpitz-acpi-0", "temp1", "temp1_input")
    NVME_SENSORS = ("nvme-pci-0100", "Composite", "temp1_input")
    FAN_SENSORS = ("emc2103-i2c-4-2e", "fan1", "fan1_input")


def main():
    logging.basicConfig(filename='odroidn2temp.log', filemode='w',
                        format='%(asctime)s %(levelname)-8s %(name)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info("OdroidN2 Temp")

    cmd = Cmd(Config.CMD)
    cmd.run()
    json_output: JsonOutput = cmd.get_json_output()
    json_output.log()

    json_parser: JsonParser = JsonParser(json_output)
    cpu = json_parser.get_cpu_sensor_temp(Config.CPU_SENSORS)
    acpi = json_parser.get_acip_sensor_temp(Config.ACPI_SENSORS)
    nvme = json_parser.get_mvne_sensor_temp(Config.NVME_SENSORS)
    fan_rpm = json_parser.get_fan_rpm(Config.FAN_SENSORS)
    # logger.info("CPU: {}".format(cpu))
    # logger.info("ACPI: {}".format(acpi))
    # logger.info("NVME: {}".format(nvme))

    data = dict(name="OdroidN2Temp", cpu=cpu, acpi=acpi, nvme=nvme, fan_rpm=fan_rpm)
    logger.info(data)

    mqttc = MqttClient(Config.MQTT.get("url"), Config.MQTT.get("port"))
    mqttc.publish('home/server/OdroidN2Temp', json.dumps(data))
    mqttc.disconnect()


if __name__ == '__main__':
    main()
