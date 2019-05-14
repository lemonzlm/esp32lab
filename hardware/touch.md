# 触摸传感器

## 概要

ESP32自带了一些可用的触摸传感器。本节教程为大家介绍这些触摸传感器。

## 硬件资源

ESP32 提供了多达 10 个电容式传感 GPIO，**能够探测由手指或其他物品直接接触或接近而产生的电容差异。**

![img](../img/rtc-gpio.png)

上图中的紫色标记，即为具备触摸式传感器功能的GPIO引脚。

| 电容式传感信号名称 | GPIO编号 |
| :----------------- | :------- |
| TOUCH0             | GPIO4    |
| TOUCH1             | GPIO0    |
| TOUCH2             | GPIO2    |
| TOUCH3             | GPIO15   |
| TOUCH4             | GPIO13   |
| TOUCH5             | GPIO12   |
| TOUCH6             | GPIO14   |
| TOUCH7             | GPIO27   |
| TOUCH8             | GPIO33   |
| TOUCH9             | GPIO32   |

**你可以像正常的GPIO一样来使用这些触摸传感器，你甚至不需要外接的触摸设备，直接使用手来接触这些引脚即可改变这些引脚的输入。**

## 使用触摸传感器产生中断

以GPIO15 ， TOUCH3为例，我们进行如下的引脚资源配置:

```
from machine import Pin
touch3 = Pin(15, Pin.IN)
touch3.irq(trigger=Pin.IRQ_RISING,handler=lambda pin: print('%s touched!' % pin))
```

请根据以上代码提示编写一个touch_test.py的文件，在main中调用，当用手触摸GPIO15的时候触发GPIO2的亮度变化。亮度变化请参考[呼吸灯](pwm.md)