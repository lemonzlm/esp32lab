# ampy文件管理工具

Ampy是Adafruit 公司提供的用于与micropython 开发板通过串行口进行文件交互管理的一套简单工具，这样当我们在编辑器写好了程序，就可以通过ampy上传到开发板硬件上一次执行一个文件，或这一个项目。而不用向解释环境那样一句句的执行。

## 安装ampy

```shell
# for linux or mac osx
sudo pip3 install --user adafruit-ampy
# for windows
sudo pip install adafruit-ampy
```

## 获取ampy帮助

```shell
ampy --help
```

你可以看到以下用法信息

```
Usage: ampy [OPTIONS] COMMAND [ARGS]...

  ampy - Adafruit MicroPython Tool

  Ampy is a tool to control MicroPython boards over a serial connection.
  Using ampy you can manipulate files on the board's internal filesystem and
  even run scripts.

Options:
  -p, --port PORT    Name of serial port for connected board.  Can optionally
                     specify with AMPY_PORT environment variable.  [required]
  -b, --baud BAUD    Baud rate for the serial connection (default 115200).
                     Can optionally specify with AMPY_BAUD environment
                     variable.
  -d, --delay DELAY  Delay in seconds before entering RAW MODE (default 0).
                     Can optionally specify with AMPY_DELAY environment
                     variable.
  --version          Show the version and exit.
  --help             Show this message and exit.

Commands:
  get    Retrieve a file from the board. (下载开发板文件)															
  ls     List contents of a directory on the board.(列出开发板文件)
  mkdir  Create a directory on the board.(在开发板上创建目录)
  put    Put a file or folder and its contents on the board.(向开发板上传文件)
  reset  Perform soft reset/reboot of the board.
  rm     Remove a file from the board.
  rmdir  Forcefully remove a folder and all its children from the board.
  run    Run a script and print its output.(执行脚本文件)
```

## Ampy基本用法

### Ampy 上传文件到开发板

```shell
ampy --port /dev/ttyUSB0 put main.py
```

### Ampy 列出开发板文件

```shell
ampy --port /dev/ttyUSB0 ls
```

### Ampy 删除开发板文件

```shell
ampy --port /dev/ttyUSB0 rm main.py
```

<u>**切记，不可删除boot.py文件**</u>

## ampy配置

为了节省每次命令行的书写时间，可以通过配置环境变量实现。

```shell
# -------- for linux -------- #
export AMPY_PORT=/dev/ttyUSB0
# 指令就可以简化为
ampy ls
ampy put main.py
# -------- for mac osx -------- #
export AMPY_PORT=/dev/tty.SLAB_USBtoUART
ampy ls
ampy put main.py
# -------- for windows -------- #
set AMPY_PORT=COM4
ampy ls
```

也可以一次向的将他写入到用户配置文件中，这样可以防止每次都要重写设置环境变量

```shell
# -------- for linux -------- #
echo "export AMPY_PORT='/dev/ttyUSB0'" >> ~/.bashrc
# -------- for mac osx -------- #
echo "export AMPY_PORT='/dev/u.SLAB_USBtoUART'" >> ~/.bash_profile
```

## 参考

https://github.com/pycampers/ampy

