# 定时器

## 概要

本文介绍了定时器与回调函数的概念，以及如何在pycharm中使用定时器，最后用定时器控制LED进行周期的闪烁。

## 定时器与延时器的区别

定时器与`utime`模块中的`sleep`延时函数最大区别在于，延时函数期间，CPU就如同进入了睡眠，之后的事情只有等睡醒之后再做，这种情况我们称之为**阻塞**， 睡觉阻塞了cpu去完成其他的任务，必须等待CPU睡醒；而定时器是**非阻塞**的，在未到达定时器定时周期结束之前，CPU可以去做别的事情，等到定时器计时完毕，便会去通知CPU，CPU再去执行**回调函数** （在你设定闹钟之前，你决定要在闹钟响了之后去做的事情）。

定时器每个周期都会产生一次中断，然后调用特定的 **回调函数callback**, 定时器中断属于内部中断.

> #### 中断
>
> CPU的中断分为很多种，不同的中断拥有不同的优先级别。当多个中断同时发生时，计算机按照优先级来以此处理

## Timer-常用API

`Timer`类被封装在`machine`模块中。

```python
from machine import Timer
```

实例化一个`Timer`对象，传入一个任意正整数作为ID。

例如：

```
timer = Timer(1)
```

然后需要 **初始化定时器**:

```python
timer.init(period=1000, mode=Timer.PERIODIC , callback=callback)
```

- `period` 定时器执行的周期，单位是`ms`， 隔period ms 执行一次。 period取值范围： `0 < period <= 3435973836`
- `mode` 定时器的执行模式
- `Timer.PERIODIC` 周期执行
- `Timer.ONE_SHOT` 只执行一次，执行完了定时器就结束
- `callback`： 定时器的回调函数，传入的一个参数是`timer`

如果你想在callback函数里面传入其他参数，可以参照下方 **定时器控制LED闪烁** 中的 **Lambda表达式** 的方法。

```pyton
timer.init(period=period, mode=Timer.PERIODIC, callback=lambda t:led_toggle(led_pin))
```

最后，定时器使用完了记得要释放定时器资源，键盘中断并不会销毁定时器，定时器会一直产生回调函数。

```python
timer.deinit()
```

## 定时器控制LED闪烁

定时器控制LED闪烁 `timer_led_blink.py`

```python
from machine import Timer,Pin
import utime


def toggle_led(led_pin):
    '''
    LED状态反转
    '''
    led_pin.value(not led_pin.value())



def led_blink_timed(timer, led_pin, freq=10):
    '''
    led 按照特定的频率进行闪烁
    LED闪烁周期 = 1000ms / 频率
    状态变换间隔（period） = LED闪烁周期/ 2 
    '''
    # 计算状态变换间隔时间 ms
    period = int(0.5 * 1000 / freq)
    # 初始化定时器
    # 这里回调是使用了lambada表达式，因为回调函数需要传入led_pin
    timer.init(period=period, mode=Timer.PERIODIC, callback=lambda t:toggle_led(led_pin))


# 声明引脚 D2 作为LED的引脚
led_pin = Pin(2, Pin.OUT)
timer = Timer(1)    # 创建定时器对象
led_blink_timed(timer, led_pin, freq=20)
```

请将以上文件在main函数中调用执行，并观察效果。