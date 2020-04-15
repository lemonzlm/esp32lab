# 安装UART-MINIUSB驱动

在开发版上，有一片ch220芯片，用于将ttl的串行接口转换为miniUSB，因此必须在主机安装该驱动程序。

Usb-2-ttl chip ch210x driver:

[Driver download](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers)

## linux 下的驱动安装

linux 下需要知道你系统的Linux内核版本，然后选择相应的版本下载，版本查询命令：

```shell
uname -a
```

下载驱动后，解压后，进入文件夹，认真阅读安装指南CP210x_VCP_Linux_4.x_Release_Notes.txt。

Ubuntu 下的安装指南(本例中，版本为LInux4.x)

```shell
make ( your cp210x driver )
cp cp210x.ko to /lib/modules/$(uname -r)/kernel/drivers/usb/serial
insmod /lib/modules/$(uname -r)/kernel/drivers/usb/serial/usbserial.ko
insmod cp210x.ko
```

## windows, mac osx 驱动安装

下载驱动后直接运行安装程序即可。

## 检查串口驱动是否安装成功

将开发版通过USB串口数据线与电脑连接，对于Windows，请自行网上搜索如何获取设备的串口号，即com端口号。

对于Linux

```shell
# 运行如下命令
ls /dev/ttyUSB*
# 如果运行结果中有 /dev/ttyUSB0之类的则表明成功，且该端口号就是开发版串口的端口号。
```

对于Mac osx

```shell
# 运行如下命令
ls /dev/cu.*
# 如果运行结果中有 /dev/cu.SLAB_USBtoUART之类的则表明成功，且该端口号就是开发版串口的端口号。
```

# 串口监控程序安装

## linux

linux下的串口监控程序可以选择使用minicom或者picocom

```shell
# 1 安装minicom
sudo apt-get install minicom
# 2 安装picocom
sudo apt-get install picocom
```

## windows 

windows的串口监控程序使用putty，请自行在网上下载并安装。

## Mac osx

linux下的串口监控程序可以选择使用minicom或者picocom

```shell
# 1 mac osx 下安装软件需要使用home brew 软件安装管理器，如果你的机器没有安装请按照如下指令安装，如果已经安装，掠过此步骤。
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
# 2 安装minicom
brew install minicom
# 3 安装picocom
brew install picocom
```

# 串口监控程序的使用

## picocom

获取picocom的使用帮助

```shell
picocom --help
```

连接到串口，进入交互解释环境，

```shell
# 对于Linux系统
picocom -b 115200 /dev/ttyUSB0
# 对于Mac OS X系统
picocom -b 115200 /dev/cu.SLAB_USBtoUART
```

## minicom

获取minicom的使用帮助

```shell
minicom --help
```

连接到串口，进入交互解释环境，

```shell
# 对于Linux系统
minicom --device /dev/ttyUSB0
# 对于Mac OS X系统
minicom --device /dev/cu.SLAB_USBtoUART
```

请注意minicom的使用，该软件在串口调试时会经常用到