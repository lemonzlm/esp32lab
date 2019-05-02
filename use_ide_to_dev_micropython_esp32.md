# 实验五：ide集成环境下的开发调

# Pychar 环境下Mciropython的开发配置 

PyCharm 是 [JetBrains](https://www.jetbrains.com/) 推出的专业级 Python IDE。Microduino 即将推出支持 [Micropython](http://micropython.org/) 的 ESP32 核心，本文介绍如何在pycharm下配置microPython开发环境

## 前置条件

### 确认Python环境为3.5 以上版本



```shell
python3 --version
# 如果版本太低，请升级版本
sudo apt-get update
sudo apt-get upgrade python3
# 如果系统没有安装python3，请执行以下操作安装
sudo apt-get install python3
```

### 下载安装Pycharm以及micro python插件

Pycharm 有商业版本也有社区的开源版本，这里我们使用开源的社区版本（community）。[下载地址在此](https://www.jetbrains.com/pycharm/download)

![设置](https://thumbsnap.com/i/M4mqReG5.jpg?0416)

设置对话框被打开，点击“Plugins”管理插件。要增加新的插件，可以选择“Browse repositories”按钮，打开在线的插件库。在插件库中查找名为“micropython”的插件。然后安装。

![安装micropython插件](https://microduino-new.oss-cn-beijing.aliyuncs.com/upload/f4e/ba0/28c/583/63e/0f9/20b/f39/f4e6b.jpg?x-oss-process=image/resize,m_lfit,limit_1,w_700/auto-orient,0/quality,Q_80)

安装完插件后，需要重启 Pycharm 生效。

## 创建micropython项目

### 配置开发环境的python版本

创建一个 Pure Python 的项目取名为“esp32”，我们需要将此 PyCharm 项目所使用的 Python 版本从缺省的 Python2 换成 Python3。在菜单中选择“Preference”，然后选择“Project:esp32 / Project Interpreter”，然后，在 Project Interpreter 下拉框中选择 “Python 3.x”。

![配置系统python环境](https://microduino-new.oss-cn-beijing.aliyuncs.com/upload/3c4/024/744/f99/c7c/9ca/552/428/3c440.jpg?x-oss-process=image/resize,m_lfit,limit_1,w_700/auto-orient,0/quality,Q_80)

如果下拉列表中没有 Python3 选项，可以点选“Show All”来增加，点按对话框左下角的“+”，选择“Add Local...”。

![](https://microduino-new.oss-cn-beijing.aliyuncs.com/upload/284/bd8/e7e/fbf/63f/db8/8ad/249/2845b.jpg?x-oss-process=image/resize,m_lfit,limit_1,w_700/auto-orient,0/quality,Q_80)

选择“System Interpretor”标签，然后选择 Python 3

![img](https:////microduino-new.oss-cn-beijing.aliyuncs.com/upload/3f7/f94/32e/d80/36f/4dd/262/942/3f72f.jpg)

最后，需要安装micropython需要的依赖包

![依赖包](https://microduino-new.oss-cn-beijing.aliyuncs.com/upload/3cf/0cd/626/ef8/7d0/5eb/84c/f81/3cf60.jpg?x-oss-process=image/resize,m_lfit,limit_1,w_700/auto-orient,0/quality,Q_80)

依次为：

- adafruit-ampy
- docopt
- esptools
- pip 
- pylint
- pyserial
- setuptools

### 配置micropython

接下来继续在“Preference”窗口中对Micropython插件进行设置。选择“Language & Frameworks”，“MicroPython”。然后选中 “Enable MicroPython Support”，然后选择“ESP8266”（没错，暂时这个插件不完全支持 ESP32，所以选择这个 ESP8266），在 “Device path” 中输入你的 ESP32 串口，例如：“/dev/cu.SLAB_USBtoUART”，输入完成后，可以按一下“Detect”按钮检查确认一下。Windows 版本 PyCharm 直接在 Device Path 中 输入串口的名称，如“COM6”，然后按 “Detect”按钮检查确认一下。

![](https://microduino-new.oss-cn-beijing.aliyuncs.com/upload/af8/ec5/b8c/60b/d38/9b0/5ba/c61/af8ce.jpg?x-oss-process=image/resize,m_lfit,limit_1,w_700/auto-orient,0/quality,Q_80)

设置完成之后，您应该能够在“Tools”菜单中看到 “MicroPython” 选项。如果看不见，请重启一下 PyCharm。

![](https://microduino-new.oss-cn-beijing.aliyuncs.com/upload/c35/4dd/300/7c8/973/ba4/b71/3d6/c3514.jpg?x-oss-process=image/resize,m_lfit,limit_1,w_700/auto-orient,0/quality,Q_80)



