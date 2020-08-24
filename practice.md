# 实训项目清单

## 基于ESP32的环境参数发布工作站

**要求**

1. ESP32 Web Server with BME680 – Weather Station (Arduino IDE)
2. 实现基于 ESP32 的 web server
3. server 通过实时读取传感器数据，提供实时环境数据，温度，湿度，空气质量，气压
4. 建议使用 ARDUINO 平台
5. 数据通过 WEB BROWSER 浏览器浏览

[设计要求与指导](https://randomnerdtutorials.com/esp32-bme680-web-server-arduino/)

## 基于ESP-NOW协议的多点温湿度采集发布系统

**要求**

- ESP-NOW Web Server Sensor Dashboard
- 基于 ESP32 的 web server
- 两路 ESP32 环境传感工作站，由 ESP32+DHT22 实现
- 使用 ESP-NOW 通信协议
- 通过浏览器查看多点环境参数信息

[设计要求与指导](https://randomnerdtutorials.com/esp32-esp-now-wi-fi-web-server/)

## ESP32 Async Web Server - ESP32 异步服务器

**要求**

- 在 ESP32 实现异步 WEB SERVER
- ESP32 SERVER 控制 3 路输出，输出用 LED 等指示
- 安装 Async Web Server 库
- 编写网页文件，在浏览器实现异步输出控制，以 LED 灯亮或灭指示

[设计要求与指导](https://randomnerdtutorials.com/esp32-async-web-server-espasyncwebserver-library/)

## 基于 MQTT 的温湿度订阅发布系统

**要求**

- 基于 MQTT 协议
- ESP32 实现 publisher 功能，发布温度，湿度数据，采用 DHT22 传感器实现
- BROKER 采用 Mosquitto 实现，可在 PC 或树莓派实现
- 使用 PC 或者树莓派实现 subcriber

[设计要求与指导](https://randomnerdtutorials.com/esp32-mqtt-publish-dht11-dht22-arduino/)

## ESP32 MQTT 温度发布器

- 基于 MQTT 协议
- ESP32 实现 publisher 功能，发布温度，湿度数据，采用 DS18B20 传感器实现
- BROKER 采用 Mosquitto 实现，可在 PC 或树莓派实现
- 使用 PC 或者树莓派实现 subcriber

[设计要求与指导](https://randomnerdtutorials.com/esp32-mqtt-publish-ds18b20-temperature-arduino/)

## ESP32 GPIO 控制

**要求**

- 任意选择 ESP32 的输入输出控制口
- 实现相应 GPIO 的开关控制电路
- 采用 ARDUINO 实现开关控制软件

[设计要求与指导](https://randomnerdtutorials.com/esp32-digital-inputs-outputs-arduino/)

## ESP32 NTP 客户端的实现

- NTP 为网络时间协议
- 实现 ESP32 NTP 客户端
- 实时读取 NTP server 的 时间与日期
- 在终端中显示时期与日期

[设计要求与指导](https://randomnerdtutorials.com/esp32-date-time-ntp-client-server-arduino/)

## ESP32 温度报警推送器

- ESP32 Email Alert Based on Temperature Threshold (change values on web server)
- ESP32+温度传感器测量环境温度
- 当超出设定阈值，发出报警推送
- 报警推送以 EMAIL 形式推送

[设计要求与指导](https://randomnerdtutorials.com/esp32-email-alert-temperature-threshold/)

## 基于 ESP32 的 OpenWeatherMap 平台天气预报浏览器

- ESP32 HTTP GET with Arduino IDE (OpenWeatherMap.org and ThingSpeak)
- OpenWeatherMap , 开源天气预报平台
- 创建免费的 OpenWeatherMap，并获取 API
- 在 ESP32 实现 HTTP 的 get 方法
- 解析返回的 JSON 数据包，并获取时间，地点，温度，湿度等天气信息
- 在终端中显示预报信息。

[设计要求与指导](https://randomnerdtutorials.com/esp32-http-get-open-weather-map-thingspeak-arduino/)

## 基于 ESP32 自动温度调节器

- ESP32/ESP8266 Thermostat Web Server – Control Output Based on Temperature
- ESP32 测量实时温度，并自动调节温控设备
  - 高于阈值，开指示灯，开风扇
  - 低于阈值，关指示灯，关风扇
- ESP32 实现 web server 以及 web page, 用以接收温度阈值的调节
- 浏览器实现阈值温度调节

[设计要求与指导](https://randomnerdtutorials.com/esp32-esp8266-thermostat-web-server/)

##  基于ESP32的便携式温度计

- ESP32/ESP8266: DHT Temperature and Humidity Readings in OLED Display
- 采集实时温湿度
- 将温度显示在OLED屏幕

[设计要求与指导](https://randomnerdtutorials.com/esp32-esp8266-dht-temperature-and-humidity-oled-display/)

## 远程控制智能灯

- ESP32 Relay Module – Control AC Appliances (Web Server)
- 通过浏览器或者APP控制智能灯开或关
- ESP32实现WEB SERVER，用以接收来自客户端的远程开关指令
- ESP32通过GPIO控制继电器实现节能灯的开关

[设计要求与指导](https://randomnerdtutorials.com/esp32-relay-module-ac-web-server/)

## Cloud Weather 工作站

- DIY Cloud Weather Station with ESP32/ESP8266 (MySQL Database and PHP)
- ESP32实时采集环境温湿度，并通过HTTP更新云端服务器的天气数据库
- 用PC机，树莓派，或VPS（任选一个）搭建WEB SERVER 以及天气数据库
- 编写SERVER PHP SCRIPT用于接收客户请求并跟新数据库或返回实时天气数据
- 通过浏览器获取天气数据

[设计要求与指导](https://randomnerdtutorials.com/cloud-weather-station-esp32-esp8266/)

## 基于ESP32的智能锁-蓝牙开关锁

ESP32的蓝牙模块接收手机传过来的开锁命令和密码，通过判断密码是否正确来确定舵机是否转动。

- ESP32与舵机进行连接
- ESP32连接手机蓝牙
- 手机通过BLE调试助手向ESP32发送开锁命令和密码
- ESP32接收数据后判断密码是否匹配并决定舵机是否转动

[设计要求与指导](https://blog.csdn.net/ohwang/article/details/106637137)

## 基于ESP32的智能锁-修改开锁密码

通过ESP32,按键模块和SG90舵机,实现蓝牙发送相应的命令修改按键密码

- 连接ESP32和按键模块的引脚,以及ESP32和SG90舵机的引脚
- 从键盘输入密码,ESP32获取到所输入的密码并判断是否正确
- 密码验证正确后,ESP32控制舵机的转动

[设计要求与指导](https://blog.csdn.net/ohwang/article/details/107170520)

# 题目编号

1. 基于ESP32的环境参数发布工作站
2. 基于ESP-NOW协议的多点温湿度采集发布系统
3. ESP32 Async Web Server - ESP32 异步服务器
4. 基于 MQTT 的温湿度订阅发布系统
5. ESP32 MQTT 温度发布器
6. ESP32 GPIO 控制
7. ESP32 NTP 客户端的实现
8. ESP32 温度报警推送器
9. 基于 ESP32 的 OpenWeatherMap 平台天气预报浏览器
10. 基于 ESP32 自动温度调节器
11. 基于ESP32的便携式温度计
12. 远程控制智能灯
13. Cloud Weather 工作站
14. 基于ESP32的智能锁-蓝牙开关锁
15. 基于ESP32的智能锁-修改开锁密码

