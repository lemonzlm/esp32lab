# 延时函数

## 概要

实现LED闪烁最简单的方法是使用延时，这节教程就以LED灯闪烁为例，教会大家使用延时函数。

## 延时模块utime

在micropython中，系统延时需要用到`utime`模块。

该模块下有以下三个`sleep`函数：

`utime.sleep(seconds)` 以秒为单位的延时

`utime.sleep_ms(ms)` 毫秒级的延时

`utime.sleep_us(us)` 微秒级的延时

示例：

```python
# 延时1000毫秒
utime.sleep_ms(1000)
```

## 控制LED闪烁

控制LED闪烁的核心流程就是：

点亮LED --> 停顿一会儿 --> 关闭LED --> 停顿一会儿

```python
from machine import Pin
import utime

# 声明一个LED对象 （P2）
led = Pin(2, Pin.OUT)

for i in range(10):
    # 点亮LED
    led.value(1)
    # 延时 500ms
    print('亮')
    utime.sleep_ms(500)
    # 关闭LED
    led.value(0)
    # 延时500ms
    print('灭')
    utime.sleep_ms(500)
```

将上述代码以函数形式保存到另一个文件，然后在main.py中调用执行：

![](img/esp32_utime_sleep.png)