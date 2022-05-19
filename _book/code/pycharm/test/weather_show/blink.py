# blink.py
import machine


def led_blink():
    import utime
    import machine

    # 声明一个引脚 例如 D13 作为LED的引脚
    led_pin = machine.Pin(2, machine.Pin.OUT)

    while True:
        # 点亮LED -> 高电平
        led_pin.value(1)
        # 延时 500ms
        utime.sleep_ms(500)
        # 关闭LED -> 低电平
        led_pin.value(0)
        # 延时500ms
        utime.sleep_ms(500)


machine.RTC
