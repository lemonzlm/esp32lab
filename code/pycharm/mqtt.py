from umqtt.simple import MQTTClient
from machine import Pin
import machine
import micropython
#选择GPIO2引脚
pin2 = Pin(2, Pin.OUT, value=0)
# MQTT服务器地址域名为：183.230.40.39,也可以填写Onenet永久域名，mqtt.heclouds.com
SERVER = "183.230.40.39"
#设备ID
CLIENT_ID = "527521926"
#随便起个名字
TOPIC = b'esp32_mqtt_basic_control'
#产品ID
username='244754'
#设备鉴权信息，或者设备的关联APIKey，此处采用设备鉴权信息，有兴趣的同学可以先创建APIKEY,再将之与该设备关联。
password='3C71BFC80054'
state = 0
def sub_cb(topic, msg):
    global state
    print((topic, msg))
    if msg == b"on":
        pin2.value(1)
        state = 1
        print("1")
    elif msg == b"off":
        pin2.value(0)
        state = 0
        print("0")
    elif msg == b"toggle":
        state = 1 - state
        pin2.value(state)

def main(server=SERVER):
    #端口号为：6002
    c = MQTTClient(CLIENT_ID, server,6002,username,password)
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(TOPIC)
    print("Connected to %s, subscribed to %s topic" % (server, TOPIC))
    try:
        while 1:
            c.wait_msg()
    finally:
        c.disconnect()