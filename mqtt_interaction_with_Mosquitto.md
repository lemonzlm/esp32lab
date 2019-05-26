# MQTT-与自建MQTT SERVER交互

## 概要

本节课讲了MQTT协议的特性， MQTT网络里面的组成部分，以及MQTT通信数据传输的流程讲解。

**keywords** mqtt tcp/ip qos publisher subscriber

## MQTT协议简介

详情请参考课件或本实验指导的[参考资料](ref/mqtt_introduction.md)

## MQTT实验-PC端

### 开源MQTT

Mosquitto，也成为蚊子项目。Mosquitto是一个实现了MQTT 5.0, 3.1.1 and 3.1协议的broker，由MQTT协议创始人之一的Andy Stanford-Clark开发，它为我们提供了非常棒的轻量级数据交换的解决方案。

Mosquitto的开发者将其python客户端捐献给了eclipse基金会，重新命名为 Eclipse paho。

因此，开源的MQTT解决方案如下(PC端)：  

| Role                             | Project           |
| -------------------------------- | ----------------- |
| Broker                           | Mosquitto         |
| Client based on C, 命令行CLI工具 | mosquitto-clients |
| Client based on Pyton            | Eclipse paho      |

**注意**

由于不同的开源实现所支持的协议版本不同，因此在安装broker和client的时候，一定要选择协议相同的版本。

#### 安装Mosquitto

在Ubuntu上面搭建MQTT的开发环境，详情请参看官网： [mosquitto.org](https://mosquitto.org/)。

mosquitto`就是MQTT Broker的实现， `mosquitto-clients`是MQTT客户端的实现。mosquitto-clients 是一个命令行客户端，即CLI，主要包括两个命令：

- 主题发布者：mosquitto_pub
- 主题订阅者：mosquitto_sub

```shell
# 对于较新版本的Ubuntu，直接支持新版本协议的mosquitto
sudo apt-get install mosquitto mosquitto-clients 
# 对于早期较老版本的ubuntu，为了支持新版本的mosquitto，需要添加新的源
sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa
sudo apt-get update
sudo apt-get install mosquitto mosquitto-clients 
# 对于 MAX OSX
brew install mosquitto
```

#### 主题发布者：mosquitto_pub

`-t` 代表要发布的主题：topic

`-m` 代表该主题此刻所携带的信息：message

```shell
mosquitto_pub -t 'pyespcar_basic_control' -m 'MOVE_FORWARD'
```

在中端上执行上面的这条信息，等于在主题`pyespcar_basic_control` 下发布一条信息`MOVE_FORWARD`

#### 主题订阅者：mosquitto_sub

通过`mosquitto_sub` 指令， 在终端中订阅指定主题Topic所携带的信息数据。当主题发布者通过mosquitto_pub发布关于该主题的信息时，订阅者就可以自自动接收到该消息。

```shell
mosquitto_sub  -t 'pyespcar_basic_control'
```

#### PC端的测试实验

打开终端的两个窗口， 首先订阅主题"pyespcar_basic_control"。

```shell
mosquitto_sub  -t 'pyespcar_basic_control'
```

然后尝试打开另一个终端，发布关于主题"pyespcar_basic_control"的信息，-m 后的参数为携带的信息：

```shell
mosquitto_pub -t 'pyespcar_basic_control' -m 'MOVE_FORWARD'
mosquitto_pub -t 'pyespcar_basic_control' -m 'This is a test message for your subscriptoion.'
```

运行效果如下图：

![img](img/mosquitto_sub_pub_cli.png)

注： 因为在同一台机器实验，因此Server的默认IP就是`localhost`，端口号默认就是`1883`，所以这里不需要指定。 更详细的参数介绍见官方文档：

- [mosquitto_pub/doc](https://mosquitto.org/man/mosquitto_pub-1.html)
- [mosquitto_sub/doc](https://mosquitto.org/man/mosquitto_sub-1.html)

### MQTT Python客户端：paho-mqtt

MQTT的客户端有多重编程语言的实现，不同语言对MQTT的版本以及功能支持均不同，我这里选用 Python语言版本的， paho-mqtt。详情请参见官网https://www.eclipse.org/paho/.

> The Eclipse Paho project provides open-source client implementations of MQTT and MQTT-SN messaging protocols aimed at new, existing, and emerging applications for the Internet of Things (IoT).

#### 安装paho-mqtt

```shell
pip3 install paho-mqtt
```

#### 使用paho-mqtt实现主题订阅

```python
# pc/paho-mqtt-subsriber.py
import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    '''处理message回调'''
    print('topic: {}'.format(msg.topic))
    print('message: {}'.format(str(msg.payload)))

# 建立一个MQTT的客户端
client = mqtt.Client()
# 绑定数据接收回调函数
client.on_message = on_message

HOST_IP = 'localhost' # Server的IP地址
HOST_PORT = 1883 # mosquitto 默认打开端口
TOPIC_ID = 'pyespcar_basic_control' # TOPIC的ID

# 连接MQTT服务器
client.connect(HOST_IP, HOST_PORT, 60)
# 订阅主题
client.subscribe(TOPIC_ID)

# 阻塞式， 循环往复，一直处理网络数据，断开重连
client.loop_forever()
```

#### 使用paho-mqtt实现发布

```Python
# pc/paho-mqtt-publisher.py
import paho.mqtt.client as mqtt
import time

HOST_IP = 'localhost' # Server的IP地址
HOST_PORT = 1883 # mosquitto 默认打开端口
TOPIC_ID = 'pyespcar_basic_control' # TOPIC的ID

# 创建一个客户端
client = mqtt.Client()
# 连接到服务器（本机）
client.connect(HOST_IP, HOST_PORT, 60)

count = 0
while True:
    count += 1
    # 待发送的数据
    message = 'This is a test message of paho clinet from publisher,{}'.format(count)   
    # 通过mqtt协议发布数据给server
    client.publish(TOPIC_ID, message)
    # 打印日志
    print('SEND: {}'.format(message))
    # 延时1s
    time.sleep(1)
```

#### 测试

可以在本地的终端打开两个串口，分别输入指令:

```shell
# 运行订阅者
python3 paho-mqtt-subsriber.py
# 运行发布者
python3 paho-mqtt-publisher.py
```

其效果与上文的`Mosquitto-client` 的CLI例程差不多。

![](/Users/lemon/Library/Mobile Documents/com~apple~CloudDocs/git/esp-lab/img/mqtt_paho_test.png)

左边是接收者的进程， 右边是发送者的进程， 这里大家留意一下，接收者在接收的时候数据打印出来是这样的：

```
topic: pyespcar_basic_control
message: b'This is a test message of paho clinet from publisher,1'
```

这里的`b'MOVE FRORWORD,175'` 是字节bytes类型的数据， 在Http通信的过程中数据以`utf-8` 编码的方式，传递字节数据。

通过`decode`方法， 可以把bytes类型的数据转换为字符串。

```python
In [1]: bdata = b'This is a test message of paho clinet from publisher,1'
In [2]: bdata.decode('utf-8')
Out[2]: 'This is a test message of paho clinet from publisher,1'
```

## MQTT与ESP32-MicroPython

之前的实验都是在Ubuntu的本机上测试的，下面就以ESP32为客户端，实现MQTT的基本发布和订阅流程。实验的角色安排如下：

| Role      | Machine                                  |
| --------- | ---------------------------------------- |
| Broker    | 安装了Mosquitto的PC 机                   |
| Subcriber | NodeMCU-32S                              |
| Publisher | NodeMCU-32S，可以与Subcriber相同也可不同 |

------

**确保所有参与的机器接入到网络，可以接入到同一LAN之内！**

---

### 确定Broker 的IP地址

查看PC当前的IP, 在Ubuntu(Broker)的命令行里面执行指令：

```python
# 一般而言，使用ifconfig可以查询IP地址。
lemon@ubuntu:~$ 
ifconfig
ens33: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.3.185  netmask 255.255.255.0  broadcast 192.168.148.255
        inet6 fe80::774f:1ead:4739:d7ad  prefixlen 64  scopeid 0x20<link>
        ether 00:0c:29:6a:c7:70  txqueuelen 1000  (Ethernet)
        RX packets 558719  bytes 770300387 (770.3 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 154949  bytes 11575873 (11.5 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 2006  bytes 172768 (172.7 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 2006  bytes 172768 (172.7 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

# 对于基于debian 9 等新的系统，改为更先进的IP指令，如下：
lemon@ubuntu:~$ 
ip -4 a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    inet 192.168.3.185/24 brd 192.168.148.255 scope global dynamic noprefixroute ens33
       valid_lft 1542sec preferred_lft 1542sec
```

如上述例子，**192.168.3.185** 为broker的IP地址。

### 使用umqtt实现subscriber

```python
# umqtt_subscriber.py
from umqtt.simple import MQTTClient
import time
# 请填入你自己BROKER的IP地址
SERVER = '192.168.3.185' 
CLIENT_ID = 'PYESPCAR_A0'
TOPIC = b'pyespcar_basic_control'

def mqtt_callback(topic, msg):
    print('topic: {}'.format(topic))
    print('msg: {}'.format(msg))


client = MQTTClient(CLIENT_ID, SERVER)
client.set_callback(mqtt_callback)
client.connect()

client.subscribe(TOPIC)


while True:
    # 查看是否有数据传入
    # 有的话就执行 mqtt_callback
    client.check_msg()
    time.sleep(1)
```

### 使用umqtt实现publisher

```python
# umqtt_publisher.py
from umqtt.simple import MQTTClient
import time
# 请填入你自己BROKER的IP地址
SERVER = '192.168.3.185'
CLIENT_ID = 'PYESPCAR_A0' # 客户端的ID
TOPIC = b'pyespcar_basic_control' # TOPIC的ID

client = MQTTClient(CLIENT_ID, SERVER)
client.connect()


while True:
    client.publish(TOPIC, 'helloworld')
    time.sleep(1)
```

注意在Esp32里面`TOPIC`需要是`bytes`类型。

#### 综合实验

1. 参考以上给出的代码，将Publisher和subcriber写成模块
2. 以pc端的paho-mqtt 作为 publisher，esp32作为subcriber，进行消息传输测试。
3. 以pc端的paho-mqtt 作为 subcriber，esp32作为publisher，进行消息传输测试。

## 延伸实验

1. 请参考实验[触摸传感器](hardware/touch.md)，在Pc 端使用paho-mqtt编写一个模块，可以远程控制ESP32开发板GPIO2所对应蓝灯的亮度。
2. 请参考实验[检测DHT传感器数据并通过socket上传](upload_dht11_data_via_socket.md)，在ESP端作为publisher, 每隔100ms检测一次DHT11的温度与湿度信息发布，在Pc 端使用paho-mqtt编写一个模块作为subcriber，实时接收DHT11传感器信息。
3. 有条件的同学，可以再树莓派等单独硬件，或者VPS上部署Broker。