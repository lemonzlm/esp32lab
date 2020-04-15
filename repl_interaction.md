# 交互式解释环境以及文件上传

## 什么是REPL

REPL是以下四个英语单词的首字母缩写：

- Read 
- Evaluate 
- Print 
- Loop 

这四个单词准确的概括了交互式解释器环境的特点，因此REPL通常也就代指**交互式解释器环境**。

## 连接REPL

与python相同，micropython的固件烧录到开发版后，系统启动后自动进入REPL，使用minicom或者picocom链接到串口。就进入了repl，详情请参看[串口操作](ref/serial_driver.md)。

```python
>>>
```

## 在REPL中执行代码

此时，可以输入micropython的代码执行命令。

```python
# 查看系统帮助
>>> help()
# 查看micropython 所有的模块
>>> help("modules")
# 倒入os模块
>>> import os
# 查看当前目录下的文件
>>> os.listdir()
```

### 点亮LED灯

首先导入`machine` 模块，machine模块几乎包含了整个ESP32的硬件资源的接口。

```python
>>> import machine
```

然后写入`machine.` 按下`Tab`按键

```python
>>> machine.
```

> #### 必备技能TAB
>
> `TAB` 可以补全代码，在一个模块后输入`.`然后使用`TAB`键可以提示出该模块中的所以内容

然后我们就可以看到machine下都有哪些子模块。

> 随着MicroPython版本的迭代，可能你看到的选项和以下的有所出入。

```python
>>> machine.
__name__        mem8            mem16           mem32
freq            reset           unique_id       idle
disable_irq     enable_irq      time_pulse_us   Timer
WDT             Pin             Signal          TouchPad
ADC             DAC             I2C             PWM
SPI             UART
```

NodeMCU32-S开发板上有一个蓝色的LED， 由P2引脚的输出来控制，高电平亮，低电平灭，因此我们可以控制P2引脚的输出来点亮该LED：

声明一个管脚，GPIO编号为2，在板子的引脚上标记为P2, 模式为输出模式，即设置为`machin.Pin.OUT`

```python
>>> pin2 = machine.Pin(2, machine.Pin.OUT)
```

管脚写入高电平

```python
>>> pin2.value(1)
```

这时你应该可以看到该led灯被点亮，散发出宝石般的蓝色光芒。

### REPL快捷键

在MicroPython的REPL里面有一些控制指令的快捷键。

- `CTRL + C` 中断程序
- `CTRL + D` 软重启
- `CTRL + E` 进入代码片段粘贴模式

```
  CTRL-A        -- on a blank line, enter raw REPL mode
  CTRL-B        -- on a blank line, enter normal REPL mode
  CTRL-C        -- interrupt a running program
  CTRL-D        -- on a blank line, do a soft reset of the board
  CTRL-E        -- on a blank line, enter paste mode
```

### 批量代码运行模式

`CTRL-E`  进入粘贴模式，批量运行代码，请编写一段代码，或者拷贝一下代码，并将其粘贴运行

```python
'''
功能介绍： LED闪烁例程
'''
import utime
import machine

# 声明一个引脚 例如 D13 作为LED的引脚
led_pin = machine.Pin(13, machine.Pin.OUT)

while True:
    # 点亮LED -> 高电平
    led_pin.value(1)
    # 延时 500ms
    utime.sleep_ms(500)
    # 关闭LED -> 低电平
    led_pin.value(0)
    # 延时500ms
    utime.sleep_ms(500)
```

> **注意**
>
> - 不能使用`ctrl+v` 粘贴，需要使用右键的粘贴功能。
> - 粘贴好代码后，不要尝试修改粘贴好的代码，或者追加

最后，终端会出现如下提示，请根据需要取消执行或确认执行。

```python
>>> 
paste mode; Ctrl-C to cancel, Ctrl-D to finish
=== 
```

### 断开与REPL的连接

Windows下，你可以直接关闭putty的窗口。

Linux或Mac下，你也可以选择直接关闭你的终端窗口。更为科学的方法是要退出`picocom`或者`minicom` ，即可断开与ESP32开发板的连接，需要依次使用到如下的快捷键：

**对于picocom**

- 先按 `ctrl + a`
- 再按`Ctrl + Q`

**对于minicom**

`ctrl + X`



