# 固件烧录

## 下载固件

首先，请下载Micropython固件，本实验使用esp32芯片，请前往[下载地址](http://micropython.org/download#esp32)。下载时，选择standard firmware (latest)。

## 安装烧录工具

Esp32 的烧录工具是esptool.py，可见它由python写成，因此需要你的操作系统预先安装python，或者python3。

```shell
# 对于python2
pip install esptool
# 对于python3
pip3 install esptool
```

## 烧录固件

1. 第一次使用时，需要先擦除固件，以后则可以直接烧录。

   ```shell
   # linux
   esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
   # mac osx
   esptool.py --chip esp32 --port /dev/cu.SLAB_USBtoUART erase_flash
   ```

   

2. 烧录固件

   ```shell
   # linux, 请调整固件文件名为你下载的文件，本例中为：esp32-bluetooth.bin
   esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-bluetooth.bin
   # mac osx 请调整固件文件名为你下载的文件，本例中为：esp32-bluetooth.bin
   esptool.py --chip esp32 --port cu.SLAB_USBtoUART --baud 460800 write_flash -z 0x1000 esp32-bluetooth.bin
   ```

   

3. 

