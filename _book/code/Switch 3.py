from machine import PWM
from machine import Pin

class Switch():
    """
    创建一个开关类
    """
    def __init__(self, pin, freq=1000):
        """
        初始化绑定一个引脚,设置默认的PWM频率为1000
        """
        self.pwm = PWM(pin,freq=freq)

    def change_duty(self, duty):
        """
        改变占空比
        """
        if 0 <= duty and duty <= 1023:
            self.pwm.duty(duty)
        else:
            print('警告：占空比只能为 [0-1023] ')

    def deinit(self):
        """
        销毁
        """
        self.pwm.deinit()