# ESP32 GPIO控制

在学习使用之前，请先学习并参考[硬件引脚说明](ref/nodemcu_32s_pin_description.md)

## GPIO

### 概要

熟练的掌握和使用芯片的IO资源是开发硬件的前提。本节主要讲解`machine` 模块中的`Pin`类的使用。回顾之前实验REPL环境的代码

```python
>>> from machine import Pin
>>> led = Pin(2, Pin.OUT) #NodeMCU-32S默认的2号GPIO与板载的LED相连
>>> led.value(1) 
```

在第一行代码中，我们从`machine`模块中导入了`Pin`这个类。

我们使用`TAB` 按键来查看`Pin`中所包含的内容：

```
>>> Pin.
__class__       __name__        IN              IRQ_FALLING
IRQ_RISING      OPEN_DRAIN      OUT             PULL_DOWN
PULL_UP         WAKE_HIGH       WAKE_LOW        init
irq             value
```

当然，更为方便的方法是在pycharm中的自动补齐功能中查看。需要注意的是，由于pycharm目前支持的ESP2866，因此有些类的支持不完整。

为了能够熟练的掌握GPIO的用法(其他的也一样)，必须要熟悉他的API。

### API详解

#### 宏定义

下面的宏定义用于配置pin，也就是将对应编号的真实的管脚配置成输入或者输出或者其他模式。

| 宏定义          | 含义               |
| :-------------- | :----------------- |
| Pin.IN          | 信号输入           |
| Pin.OUT         | 信号输出           |
| Pin.PULL_DOWN   | 是否接入下拉电阻   |
| Pin.PULL_UP     | 是否接入上拉电阻   |
| Pin.IRQ_RISING  | 信号上升沿触发中断 |
| Pin.IRQ_FALLING | 信号下降沿触发中断 |
| Pin.WAKE_HIGH   | 从高电平唤醒       |
| Pin.WAKE_LOW    | 从低电平唤醒       |
| Pin.OPEN_DRAIN  | 开漏               |

**注意：不是每个端口都有下面的全部属性。例如某些引脚只能输入不能输出**

我们注意到其中的`Pin.OUT`为信号输出，而`Pin(2, Pin.OUT)`，就是将GPIO2 设置为输出模式，

通过改变该GPIO的`value`为逻辑1，于是便在该引脚上输出了高电平(3v以上的电压)，该led灯便被点亮。

#### 类

##### class machine.Pin(id[, mode[, pull[, value]]])

`id`：任意引脚号
`mode`：引脚模式

- `Pin.IN` — 输入
- `Pin.OUT` — 输出
- `Pin.OPEN_DRAIN` — 开漏

`pull`：是否接入拉电阻

- `None` — 无上拉、下拉电阻
- `Pin.PULL_UP` — 上拉
- `Pin.PULL_DOWN` — 下拉

`value`：引脚电平状态

- `0` —低电平
- `1` —高电平

##### 定义Pin

示例：

```python
>>> from machine import Pin
>>> 
>>> led = Pin(2, mode=Pin.OUT, pull=None, value=0)  #可以简单使用Pin(2, Pin.OUT)
>>> print(led)
Pin(2)
```

#### 函数

##### Pin.init([mode[, pull]])

函数说明：初始化引脚。

`mode`：

- `Pin.IN` — 输入
- `Pin.OUT` — 输出
- `Pin.OPEN_DRAIN` — 开漏

`pull`：

- `None` — 无上拉、下拉电阻
- `Pin.PULL_UP` — 上拉
- `Pin.PULL_DOWN` — 下拉

示例：

```python
>>> from machine import Pin
>>> pin = Pin(2)
>>> pin.init(mode=Pin.OUT)  #也可以写作pin.init(Pin.OUT)
```

##### Pin.value([value])

函数说明：获取或设置引脚电平状态，根据引脚的逻辑电平返回0或1。 
**注意：不带参数时是读取输入电平，带参数时是设置输出电平。**

`value`：可以是`True`/`False`，也可以是`1`/`0`。

示例：

```python
>>> pin = Pin(2,Pin.OUT)
>>> pin.value()
0
>>> pin.Value(True)
>>> pin.value()
1
>>> pin.Value(0)
>>> pin.value()
0
```

##### Pin.irq(trigger, handler)

函数说明：配置一个引脚的中断处理程序，在引脚的电平满足条件时调用。

`trigger`：

- `Pin.IRQ_FALLING` — 下降沿触发
- `Pin.IRQ_RISING` — 上升沿触发

`handler`：中断被触发之后的回调函数

示例：

```
>>> touch = Pin(32, Pin.IN)
>>> touch.irq(trigger=Pin.IRQ_FALLING, handler=lambda t:print("IRQ triggered by your finger"))
```

![img](../img/touch-irq.png)

> #### 触摸传感器
>
> ESP32上的部分引脚自带触摸式的传感器，我们可以直接通过触摸来改变这些引脚的电平输入，在之前的引脚的讲解中，之后我们会详细为大家介绍

然后你便可以在REPL中看到：

![](../img/esp32_touch_test.png)