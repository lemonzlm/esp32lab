# 基础开发调试

## REPL:命令行交互解释开发

如上一章，我们可以在交互式解释环境下进行代码的开发调试，但是显然这样的方法效率很低，只适合于初学者认识 MicroPython 的环境以及模块。

虽然`REPL` 也提供了粘贴模式运行代码，但是对于大型的代码调试，仍然不是高效的方法。

因此，这种交互解释方式，只适合学习环境下使用，在生产环境下应该采用其他更为高效的编辑器和 IDE。

## 代码编辑器与源代码管理

常见的流行编辑器包括：

- Pycharm (python)
- Vs code (各种语言)
- Arduino (物联网语言开发)

常见的适用于 micropython 的代码管理工具

- [Ampy](ref/ampy_usage.md)
- [Rshell](ref/rshell_usage.md)
- [mpfshell](ref/mpfshell_usage.md)

### 采用 pycharm community 编辑代码

#### 下载编辑器

Pycharm 因为是商业软件，不能直接使用，我们这里采用 pycharm community 版本，该版本免费开放，已经够我们实验使用，请前往[下载](https://www.jetbrains.com/pycharm/download/#section=linux)。

![请注意下载community版本](img/download_pycharm_ide_community.png)

#### 配置编辑器

有关 pycharm 的具体使用参见[Pycharm 环境下 Mciropython 的开发配置](pycharm_dev.md), 本节课不用配置，只需要书写代码，体验其特性即可。

#### 编写代码

利用这个编辑器，编写一个让蓝灯交闪烁的代码，将其命名为`main.py`。

参考代码如下：请认真分析一下参考代码的每一句。

```python
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
```

### 管理代码

#### 利用 ampy 管理代码

Ampy 上传文件到开发板

```shell
ampy --port /dev/ttyUSB0 put main.py
```

上传完成后，观察开发板的蓝灯是否交替闪烁，如果不成功，请修改代码重新上传。

#### 利用 rshell 管理代码

```shell
rshell
cp main.py /pyboard/
```

### 提高练习

请根据以上的实验内容，修改代码，要求将闪烁 LED 灯的功能封装到另一个文件中，如 led_blink.py, 由 main.py 来调用。

### 采用 VS Code 编辑并管理代码

VS Code 对 python 的支持极好，但是对于 MicroPython 的支持相对较弱，不但缺少相应的代码补全等必要的编辑功能，同时也缺乏必要的代码管理功能，如：文件上传，烧录，在线运行等调试等功能。

自从正点原子团队发布了 RT-Thread MircoPython 插件后，情况得到了很大的改善。该插件目前支持 STM32，ESP32, ESP2866 等芯片，详情请参见 [RT-Thread MicroPython](https://github.com/RT-Thread-packages/micropython)。

本插件目前是 VSCODE 环境下相对较好的 MicroPython 插件。**推荐使用**。

由于该插件推出时间不长，其稳定性仍需验证以及更长时间的版本升级迭代。依据目前测试情况，其在 Mac OSX，Ubuntu18 下无重大 BUG 报告。Windows 下，本人未做相应测试，因此不可知。

## 定制 IDE

IDE 的功能更为强大，不但能编辑，调试，同时还能烧录文件等。因为 ESP32 是比较新的芯片，因此配套的 IDE 还不是很成熟，主要有以下几种

### 使用 MicroPython 的 IDE

- Pycharm + micropython plugin
- **Pycharm + microPython Plugin + rshell**
- **VS Code + RT Thread Extension**

### 使用 C 语言的 IDE

- VS Code + PlatformIO Extension
- Arduino IDE
- VS Code + Expressif Extension

> **注意**
>
> 本实验指导重点在于使用 python，开始时，使用 `pycharm`
>
> 当使用 c 或 arduino 开发时，采用 `vscode + platformIO`。

接下来的两次实验我们将重点演练

- [Pycharm + microPython Plugin + rshell](pycharm_dev.md)
- [VS Code + RT Thread Extension](vscode_rt_thread_dev.md)
