# WIFI网络实验

## 实验目的

- 学习在PC机系统中网络（network）的使用方法
- 学习ESP32连接网络的使用

## 准备工作

- NODEMCU-32S 1块
- micro USB数据线 1条
- 电脑 1台
- 所需软件, pycharm, [rshell](rshell_usage.md)

## **Network库的使用方法**

网络模块用于配置WiFi连接。一共两种模式:

- 模式一:是ESP32当STA节点，即连接路由器的节点。
- 模式二，是ESP32做为AP，充当路由。

## ESP32作为STA节点模式 

请在REPL模式下使用如下函数，练习WIFI主要的操作。

```python
import network
wlan = network.WLAN(network.STA_IF)      # 创建一个站（当ESP32连接到路由器时）接口
wlan.active(True)                          # 激活接口
wlan.scan()                                 # 扫描接入点
wlan.isconnected()                         # 检查站点是否连接到路由器
wlan.connect('essid', 'password')        # 连接到路由器
wlan.config('mac')      # 获取接口的MAC地址
wlan.ifconfig()         # 获取接口的IP / netmask / gw / DNS地址

#检查是否连接是否建立
wlan.isconnected()
#检查接口是否活动
wlan.active()
#检查接口的网络设置
wlan.ifconfig()
```

以下是ESP32自动连接本地网络的代码，请根据自己的环境修改并写入到开发板。

```python
from machine import Pin
import network
import time
def led_state():
    p2 = Pin(2, Pin.OUT)
    p2.value(0)
    time.sleep_ms(500)
    p2.value(1)
    time.sleep_ms(500)
    p2.value(0)
    time.sleep_ms(500)
    p2.value(1)
    time.sleep_ms(500)
def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    p2 = Pin(2, Pin.OUT)
    sta_if.active(False)
    if not sta_if.isconnected():
        p2.value(0)
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('essid', 'password')
        while not sta_if.isconnected():
            pass
    if sta_if.isconnected():
        print('connect success')
        led_state()
        print('network config:', sta_if.ifconfig())
do_connect()
```

只需要将上面代码写入到开发板中，复位重新运行程序后，就会看到蓝灯常亮（正在连接网络），然后蓝灯交替闪烁两次，打印connect success，证明已经连接到本地网络。

## ESP32作为AP模式

以下代码是建立一个简单的WIFI AP热点代码，请根据自己的环境建立AP热点，完成以下两项任务：

1. 将自己的手机连接到该AP点
2. 一组作为AP，另一组作为sta接入该ap点。

```python
import network
ap = network.WLAN(network.AP_IF) #创建接入点接口
ap.active(True)         # 激活接口
ap.config(essid='ESP-AP',password='123456') # 设计接入点的ESSID，密码为123456
```

也可以设置无密码开放模式，如下：

```python
ap.config(essid='ESP-AP',authmode=0) # 设计接入点的ESSID，开放无密码模式
```

AuthMode有五种模式：

- 0 : OPEN
- 1 : WEP
- 2 : WPA-PSK
- 3 : WPA2-PSK
- 4 : WPA/WPA2-PSK