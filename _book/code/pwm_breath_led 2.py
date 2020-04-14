# # #import blink
# # import wifiAccess
# # #blink.led_blink()
# # wifiAccess.connect('lemon','lemon@Zlm1018')
# import wifiAp
# wifiAp.createAp()

import machine
import utime, math
from switch import Switch
from machine import Pin

switch_led = Switch(Pin(2))

def pulse(switch, period, gears):
    # 呼吸灯核心代码
    # 借用sin正弦函数，将PWM范围控制在 23 - 1023范围内
    # switch 开关对象
    # period 呼吸一次的周期 单位/毫秒
    # gears 呼吸过程中经历的亮度档位数

    for i in range(2 * gears):
        switch.change_duty(int(math.sin(i / gears * math.pi) * 500) + 523)
        # 延时
        utime.sleep_ms(int(period / (2 * gears)))

# 呼吸十次
for i in range(10):
    pulse(switch_led, 2000, 100)

# 释放资源
switch_led.deinit()