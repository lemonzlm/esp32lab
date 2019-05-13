# NodeMCU-32S引脚说明

## 引脚标注图

NodeMCU-32S 开发板左右各19个引脚，共38个，下图为NodeMCU-32S的各个引脚的详细标注。

![img](http://src.1zlab.com/micropython-esp32/pins-and-gpio/rtc-gpio.png)

------

![](img/nodemcu_32s_pin.png)

## 引脚类型以及功能

NodeMCU-32S总共拥有2排引脚，各19个，共计38个。

### 基础引脚

负责供电和使能的基础引脚共有6个：

| 名称 | 功能                   | 位置                   |
| :--- | :--------------------- | :--------------------- |
| Vin  | 用于开发板5V供电       | 上图左下角，褐色标签   |
| 3V3  | 3.3V电压输出           | 上图左上角，红色标签   |
| GND  | 共地                   | 上图黑色标签，共三个   |
| EN   | 使能端，可触发复位操作 | 上图左上角第二个，黄色 |

### GPIO

GPIO是General-purpose input/output的缩写，意思为通用型输入或输出，ESP32上的GPIO共有32个。

> **规约**
>
> NodeMCU32-S开发板背面实际印刷的是P0 - P39，上图中的标注使用的是GPIO - GPIO39
>
> 接下来的教程中我们所说的 GPIO+编号 = NodeMCU-32S开发板背面印刷的 P+编号

![img](http://src.1zlab.com/micropython-esp32/pins-and-gpio/nodemcu-32s-pins.png)

#### 未被引出的引脚编号

NodeMCU-32S的GPIO引脚共32个, 编号范围从 P0 - P39 对应于上图中的GPIO0 - GPIO39，按照编号计算应该有40个GPIO引脚，实际上ESP32这块芯片确实有这么多个GPIO，但是由于开发板的封装 等原因，以下编号的引脚在ESP32的开发板中通常未被引出：

- GPIO20 GPIO24 GPIO28 GPIO29
- GPIO30 GPIO31 GPIO37 GPIO38

#### 特殊的标注

同时，你还需要注意的是，NodeMCU-32S上对以下几个GPIO 进行了特殊标注：

| NodeMCU-32S的特殊标记 | 原GPIO编号 |
| --------------------- | :--------- |
| CLK                   | GPIO6      |
| SD0                   | GPIO7      |
| SD1                   | GPIO8      |
| SD2                   | GPIO9      |
| SD3                   | GPIO10     |
| CMD                   | GPIO11     |
| SVP                   | GPIO36     |
| SVN                   | GPIO39     |

#### 只能作为输入的GPIO

几乎所有的GPIO都能进行I/O双向输入输出控制，但是以下的几个GPIO例外，只能进行输入，而无法进行输出：

GPIO34, GPIO35, GPIO36, GPIO39

### GPIO功能分类

| 功能简介                                           | 缩写     | 可用的GPIO编号                                 | 备注                         |
| :------------------------------------------------- | :------- | :--------------------------------------------- | :--------------------------- |
| 模拟信号采样                                       | ADC      | 32, 33, 34, 35, 36, 39                         |                              |
| 模拟信号输出                                       | DAC      | 25, 26                                         |                              |
| 串行通信                                           | UART     | 1(TX0),3(RX0), 10(TX1),9(RX1) ,17(TX2),16(RX2) | 共三组                       |
| 探测由手指或其他物品直接接触或接近而产生的电容差异 | TOUCHPAD | 0, 2, 4, 12, 13, 14, 15, 27, 32, 33            |                              |
| SPI总线接口                                        | SPI      | hspi(14,12,13,15) vspi(23,19,18,5)             |                              |
| I2C总线接口                                        | I2C      | SDA(21) SCL(22)                                | MicroPython并未实现硬件的I2C |

