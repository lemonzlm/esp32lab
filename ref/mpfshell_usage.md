# mpfshell 操作指南

一个简单的基于shell的文件浏览器，用于ESP8266和基于WiPy Micropython的设备。 shell是一个帮助程序，用于向ESP8266（通过串行线和Websockets）和WiPy（串行线和telnet）上传/下载文件。它基本上提供了在设备的闪存FS上列出和上传/下载文件的命令。

## 安装

```shell
sudo pip install mpfshell
```

## 操作指南

### 开启软件脚本

```shell
$ mpfshell

** Micropython File Shell v0.9.0, sw@kaltpost.de **
-- Running on Python 3.7 using PySerial 3.4 --

mpfs [/]>
```

### 查看支持命令

```shell
mpfs [/]> help

Documented commands (type help <topic>):
========================================
EOF  cd     exec  get   lcd  lpwd  md    mput  mrm   put   pwd   rm
cat  close  exit  help  lls  ls    mget  mpyc  open  putc  repl
```

### 进入目标开发板

```shell
# 确定目标版占用的串口
$ ls /dev/cu.*
/dev/cu.Bluetooth-Incoming-Port /dev/cu.SLAB_USBtoUART

# 方法一，mpfshell <目标版串口号，注意，不要/dev/>
$ mpfshell cu.SLAB_USBtoUART
Connected to esp32

** Micropython File Shell v0.9.0, sw@kaltpost.de **
-- Running on Python 3.7 using PySerial 3.4 --
mpfs [/]>

# 方法二，进入mpfshell后在连接设备
$ mpfshell

** Micropython File Shell v0.9.0, sw@kaltpost.de **
-- Running on Python 3.7 using PySerial 3.4 --

mpfs [/]> open cu.SLAB_USBtoUART
Connected to esp32
mpfs [/]>
```

### 文件操作

```
# 列出目标版文件
ls
# 拷贝本地文件到目标版
put test.py
# 拷贝本地文件到目标版并改名为main.py
put test.py main.py
# 删除目标版文件
rm test.py
```

### 进入到REPL

```shell
repl
*** Exit REPL with Ctrl+] ***

MicroPython v1.10-298-g47e76b527 on 2019-04-18; ESP32 module with ESP32
Type "help()" for more information.
>>>
```

