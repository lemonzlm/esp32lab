# 实训项目清单

## 基于 ESP32 的环境参数发布工作站

**要求**

1. ESP32 Web Server with BME680 – Weather Station (Arduino IDE)
2. 实现基于 ESP32 的 web server
3. server 通过实时读取传感器数据，提供实时环境数据，温度，湿度，空气质量，气压
4. 建议使用 ARDUINO 平台
5. 数据通过 WEB BROWSER 浏览器浏览

[设计要求与指导](https://randomnerdtutorials.com/esp32-bme680-web-server-arduino/)

## 基于 ESP-NOW 协议的多点温湿度采集发布系统

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

## 基于 ESP32 的便携式温度计

- ESP32/ESP8266: DHT Temperature and Humidity Readings in OLED Display
- 采集实时温湿度
- 将温度显示在 OLED 屏幕

[设计要求与指导](https://randomnerdtutorials.com/esp32-esp8266-dht-temperature-and-humidity-oled-display/)

## 远程控制智能灯

- ESP32 Relay Module – Control AC Appliances (Web Server)
- 通过浏览器或者 APP 控制智能灯开或关
- ESP32 实现 WEB SERVER，用以接收来自客户端的远程开关指令
- ESP32 通过 GPIO 控制继电器实现节能灯的开关

[设计要求与指导](https://randomnerdtutorials.com/esp32-relay-module-ac-web-server/)

## Cloud Weather 工作站

- DIY Cloud Weather Station with ESP32/ESP8266 (MySQL Database and PHP)
- ESP32 实时采集环境温湿度，并通过 HTTP 更新云端服务器的天气数据库
- 用 PC 机，树莓派，或 VPS（任选一个）搭建 WEB SERVER 以及天气数据库
- 编写 SERVER PHP SCRIPT 用于接收客户请求并跟新数据库或返回实时天气数据
- 通过浏览器获取天气数据

[设计要求与指导](https://randomnerdtutorials.com/cloud-weather-station-esp32-esp8266/)

## 基于 ESP32 的智能锁-蓝牙开关锁

ESP32 的蓝牙模块接收手机传过来的开锁命令和密码，通过判断密码是否正确来确定舵机是否转动。

- ESP32 与舵机进行连接
- ESP32 连接手机蓝牙
- 手机通过 BLE 调试助手向 ESP32 发送开锁命令和密码
- ESP32 接收数据后判断密码是否匹配并决定舵机是否转动

[设计要求与指导](https://blog.csdn.net/ohwang/article/details/106637137)

## 基于 ESP32 的智能锁-修改开锁密码

通过 ESP32,按键模块和 SG90 舵机,实现蓝牙发送相应的命令修改按键密码

- 连接 ESP32 和按键模块的引脚,以及 ESP32 和 SG90 舵机的引脚
- 从键盘输入密码,ESP32 获取到所输入的密码并判断是否正确
- 密码验证正确后,ESP32 控制舵机的转动

[设计要求与指导](https://blog.csdn.net/ohwang/article/details/107170520)

## 基于 IOT 云端控制的智能书桌

**功能要求**

1. 通过无线通信技术，连接云端服务（如阿里 IOT 等），可远程监测及控制智能书桌的状态
2. 通过光敏传感器采集书桌现场光强度，根据书桌现场光强度值，由处理器自动调节 LED 灯光强度
3. 通过温度传感器采集书桌现场温度，并由处理器自动调节风扇转速
4. 若人离开书桌 1 分钟后没有回到书桌前，将控制 LED 灯和风扇关闭

**技术要求**

1. 不限定无线通信方式可以采用 WIFI, LWPAN 以及蜂窝通信（GPRS/3G/4G）,推荐使用 WIFI
2. 建议采用 ESP32/ESP2866 或 STM32 等处理器。
3. 优先采用具有操作系统的软件解决方案，编程语言不限，可采用 C, Ardoino 以及 MicroPython
4. 如有条件优先采用 PCB 实现电路
5. 应用系统基本保护功能，如果看门狗，异常报警。
6. 云端服务可以自行搭建，使用 PC 服务器，或树莓派等；也可以采用商业成熟方案, 如中国移动，阿里巴巴，或机智云，平台使用可自选。
7. 物联网协议使用不限，可采用 MQTT,HTTP,COAP 等，推荐使用 MQTT

## 基于 IOT 的智能温室控制系统

**功能要求**

1. 测量环境温度，温度高出阈值，则打开风扇降温，低于阈值在关闭
2. 测量环境湿度，湿度高出阈值，则开启加湿器，反之关闭
3. 检测土壤湿度，超出阈值，则打开水泵浇水，反之关闭
4. 检测光照，低于阈值，打开 LED 等补光，反之关闭

**技术要求**

1. 不限定无线通信方式可以采用 WIFI, LWPAN（如 lora, nbiot）以及蜂窝通信（GPRS/3G/4G）,推荐使用 WIFI
2. 建议采用 ESP32/ESP2866 或 STM32 等处理器。
3. 优先采用具有操作系统的软件解决方案，编程语言不限，可采用 C, Ardoino 以及 MicroPython
4. 如有条件优先采用 PCB 实现电路
5. 应用系统基本保护功能，如果看门狗，异常报警。
6. 云端服务可以自行搭建，使用 PC 服务器，或树莓派等；也可以采用商业成熟方案, 推荐使用商业平台，如：阿里云，机智云等。
7. 物联网协议使用不限，可采用 MQTT,HTTP,COAP 等，推荐使用 MQTT
8. 【选做】设计实现简单地手机 APP，APP 可获取并查看温室的环境数据并实现异常报警。APP 获取数据包含两种，定时同步以及主动查询。

## 空气质量检测仪的设计与实现

**功能要求**

1. 检测室内有害气体，包括：可吸入颗粒物，一氧化碳，苯以及液化气等
2. 检测环境温湿度
3. 利用液晶屏实时显示检测值
4. 检测值超出设定阈值发出声光报警
5. 同步检测数值到手机或云端服务器**（选做）**

**技术要求**

1. 建议采用 ESP32/ESP2866 或 STM32 等处理器。
2. 优先采用具有操作系统的软件解决方案，编程语言不限，可采用 C, Ardoino 以及 MicroPython
3. 设计中应包含传感检测模块，显示模块，以及通信模块（可选）
4. 系统基本保护功能，如果看门狗，异常报警。
5. **选做：**设计并实现简单地 APP，实现实时数据上传到手机 APP（WIFI 或蓝牙）
6. **选做：**实现 IOT 平台搭建，实现一起数据实时同步至 IOT 云端平台。推荐使用商业平台，如：阿里云，机智云等。

[参考](https://www.cirmall.com/circuit/4904)

## 智能门锁的设计与实现

功能要求

1. 可实现三种种开锁方式：指纹开锁、密码开锁、RFID/NFC 开锁。任选两种开锁方式
2. 指纹录入与存储，可管理多个指纹，包括录入，修改，删除等操作
3. 密码录入与存储，可管理多个密码，包括录入，修改，删除等操作。
4. RFID/NFC 卡片管理，可管理多个卡片，包括录入，修改，删除等操作。
5. 带有液晶显示屏，默认进入待机关闭状态，主要作为指纹以及密码操作的 UI 界面
6. 具备语音提示功能

技术要求

1. 建议采用 ESP32/ESP2866 或 STM32 等处理器。
2. 优先采用具有操作系统的软件解决方案，编程语言不限，可采用 C, Ardoino 以及 MicroPython
3. 系统基本保护功能，如果看门狗，异常报警。

[参考](https://www.cirmall.com/circuit/13903)

## 家用智能锁的设计与实现

功能要求

1. 可实现三种种开锁方式：密码开锁、RFID/NFC 开锁。任选一种开锁方式
2. 密码录入与存储，可管理多个密码，包括录入，修改，删除等操作。
3. RFID/NFC 卡片管理，可管理多个卡片，包括录入，修改，删除等操作。
4. 带有液晶显示屏，默认进入待机关闭状态，主要作为指纹以及密码操作的 UI 界面
5. 具备语音提示功能
6. 手机控制功能：设置密码/卡片，设置密码/卡片，远程开关锁

技术要求

1. 建议采用 ESP32/ESP2866 或 STM32 等处理器。
2. 优先采用具有操作系统的软件解决方案，编程语言不限，可采用 C, Ardoino 以及 MicroPython
3. 系统基本保护功能，如果看门狗，异常报警。
4. 设计并实现简单的 APP 或者小程序，实现远程设置锁，开关锁等操作。采用 WiFi 或蓝牙。

[参考](https://www.cirmall.com/circuit/13903)

## 网络监控摄像头的设计与实现

功能要求

1. 摄像头像素不低于 200 万
2. 可语音唤醒（选做）
3. 制作简单手机 APP, 通过互联网远程串流摄像头实时视频
4. 摄像头连接至 IOT 云端实现设备管理（阿里云或机智云等）
5. 可实现人脸识别，当检测到陌生人或物时发出语音报警同时报警到手机 APP 或云端。

技术要求

1. 推荐使用集成模组 ESP-CAM 或 ESP-EYE
2. 优先采用具有操作系统的软件解决方案，编程语言不限，可采用 C, Ardoino 以及 MicroPython
3. 系统基本保护功能，如果看门狗，异常报警。

[参考](https://my.oschina.net/iotexplorer/blog/4403133)

[参考](https://www.cirmall.com/circuit/12841)

## 基于人脸识别的存储柜设计与实现

**功能要求**

1. 人脸学习以及存储管理
2. 可实现人脸匹配，如果匹配，则打开柜门
3. 长时间检测不到正常人脸后，自动关门（选做）
4. 必要的报警功能，如：未关门等。

**技术要求**

1. 推荐使用集成模组 ESP-CAM 或 ESP-EYE
2. 优先采用具有操作系统的软件解决方案，编程语言不限，可采用 C, Ardoino 以及 MicroPython
3. 系统基本保护功能，如果看门狗，异常报警。

## 基于 RFID 的门禁卡的设计与实现

功能要求

1. 门禁锁开锁方式有两种：RFID 卡片与人脸识别（可选）
2. 设备带有触摸屏，用于显示和操作门禁系统。
3. 具有卡片管理功能：如添加，更改，删除等。
4. RFID 配对则驱动电机开门，RFID 不配对，则提示匹配错误
5. 人脸录入功能（可选）

技术要求

1. 推荐使用 STM32/ESP32 等 MCU，或使用集成模组 ESP-EYE
2. 优先采用具有操作系统的软件解决方案，编程语言不限，可采用 C, Ardoino 以及 MicroPython
3. 系统基本保护功能，如果看门狗，异常报警。

[参考](https://www.cirmall.com/circuit/19144)

## 智能 WIFI 插座的设计与实现

功能要求

1. 在传统插座的基础上，设计基于 WIFI 控制的远程控制插座
2. 可控制多路插座开关
3. 设计简单的手机 APP 或微信小程序，远程设定插座的开与关状态
4. 实现局域网内开关控制（必做）
5. 实现因特网内开关控制（选做），设备与手机均连接到第三方 IOT 平台，采用 MQTT 协议进行控制，第三平可采用阿里云，机智云或中移动 ONENET 等。

技术要求

1. 推荐使用 ESP32/STM32 等 MCU
2. 优先采用具有操作系统的软件解决方案，编程语言不限，可采用 C, Ardoino 以及 MicroPython
3. 系统基本保护功能，如果看门狗，异常报警。

参考

## 蓝牙网关的设计与实现

功能要求

1. 网关包含一路 WIFI 和至少两路蓝牙 MASTER。
2. 实现蓝牙设备与网关的配对连接
3. 网关通过 WiFi 连接云端 IOT 服务，如阿里云 IOT 或机智云等。
4. 设计简单的 APP，通过手机 APP 操作在云端管理蓝牙节点设备，如果设备添加，删除等操作
5. 设计简单的蓝牙侧空节点，带有一路 LED 灯和温湿度检测
6. 将温湿度发布到 IOT 云端，手机端 APP 订阅该服务，在 APP 上显示实时温湿度。
   通过手机 APP 发布开灯指令到云端，蓝牙节点订阅该服务并实现实时开关灯。

技术要求

1. 蓝牙网关推荐使用 ESP32/STM32 等 MCU，或树莓派。蓝牙节点建议采用 ESP32
2. 优先采用具有操作系统的软件解决方案，编程语言不限，可采用 C, Ardoino 以及 MicroPython
3. 系统基本保护功能，如果看门狗，异常报警。
4. 协议建议使用 MQTT

参考

## 基于 LORA 的土壤湿度检测传输系统

**功能要求**

1. 采用 Lora 点对点透传模式，即只使用 Lora 物理层进行传输
2. 系统包含一个基站节点，N 个检测节点（实际实现中只需要一个即可），检测节点分时轮询方式与基站节点通信。
3. 设计轮询访问控制协议，并在基站节点和检测节点分别实现。
4. 检测节点要求
5. 配置外接土壤湿度传感器，实时检测土壤湿度并通过 Lora 透传至基站节点
   采用低功耗设计
   采用电池供电
6. 基站节点要求
7. 管理 N 个检测节点
   接收来自节点的湿度数据
   将收到的信息显示在设备显示屏
   设计联网功能（通过 WiFi 或蜂窝通信），将数据发布到服务器或 IOT 云端。（选做）
8. 两个节点的 lora 通信模块可提供使用，无需重新购买。

**技术要求**

1. 采集节点尽量遵循低功耗设计，MCU 在满足条件情况下选择 ULPBench 分数高的。建议使用轻量级操作系统，采用 C 编程。
2. 基站节点强调性能，可采用 ARM-CORTEX-A 系统处理器，也可采用 STM32F/ESP32 系列。
3. 基站节点可交流供电，也可直流电池供电，设计充电电路。
