import logging
import paho.mqtt.client as mqtt


class MqttClient:
    def __init__(self, url: str, port: int) -> None:
        self._logger = logging.getLogger(__name__)
        self._url = url
        self._port = port
        self._connected = False
        self._mqttc = None
        self._connect()

    def _connect(self):
        try:
            self._mqttc = mqtt.Client(client_id="OdroidN2Temp@jarvis",
                                      clean_session=True,
                                      userdata=None,
                                      protocol=mqtt.MQTTv31)

            self._mqttc.on_log = self._on_log
            self._mqttc.connect(host=self._url, port=self._port, keepalive=60)
            self._connected = True
        except ConnectionRefusedError as e:
            self._logger.fatal('MQTT ERROR ConnectionRefusedError: ' + str(e))
        except Exception as e:
            self._logger.fatal('MQTT ERROR: ' + str(e))

    def _on_log(self, client, userdata, level, buf):
        self._logger.info('MQTT LOG BUF: ' + buf)

    def disconnect(self):
        self._logger.info('MQTT INFO: Disconnect from broker')
        self._mqttc.disconnect()

    def publish(self, topic, message):
        if self._connected:
            self._mqttc.publish(topic=topic, payload=message, qos=1, retain=False)
            self._logger.info('MQTT INFO: Message was send to broker, Topic: {}, Body {}'.format(topic, message))
        else:
            self._logger.error('MQTT ERROR: message wasn\'t sent!')
