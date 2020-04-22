
# umqtt_publisher.py
from umqtt.simple import MQTTClient
import time
def publish_topic():
    SERVER = '192.168.3.185'
    CLIENT_ID = 'PYESPCAR_A0' # 客户端的ID
    TOPIC = b'pyespcar_basic_control' # TOPIC的ID
    # 连接broker
    client = MQTTClient(CLIENT_ID, SERVER)
    client.connect()

    while True:
        client.publish(TOPIC, 'helloworld')
        time.sleep(1)