# ESP-IDF 开发基本过程

## 配置ESP-IDF

### 获取工具链的依赖包

```shell
# for debian or ubuntu
sudo apt-get install gcc git wget make libncurses-dev flex bison gperf python python-pip python-setuptools python-serial python-cryptography python-future python-pyparsing
```

### 获取工具链

```shell
# dowload tool chain
mkdir -p ~/esp
cd ~/esp
wget https://dl.espressif.com/dl/xtensa-esp32-elf-linux64-1.22.0-80-g6c4433a-5.2.0.tar.gz
tar -xzf xtensa-esp32-elf-linux64-1.22.0-80-g6c4433a-5.2.0.tar.gz
# setup evn
echo 'export PATH="$HOME/esp32/xtensa-esp32-elf/bin:$PATH"' >> ~/.bashrc
```

### 获取ESP-IDF

```shell
mkdir esp
cd esp
git clone --recursive https://github.com/espressif/esp-idf.git
```

### 配置环境变量

```shell
## for mac osx
nano ~/.bash_profile
## addlines to the file
export IDF_PATH=~/esp/esp-idf
## for ubuntu or debian
echo 'export IDF_PATH=$HOME/esp/esp-idf'>> ~/.bashrc
```

### 安装Python软件包

```shell
# esp 工程默认使用python2
python -m pip install --user -r $IDF_PATH/requirements.txt

## 对于python3
pip3 install --upgrade pip
python3 -m pip install --user -r $IDF_PATH/requirements.txt
## 对于有的系统，可能要添加Python包的环境变量,以我的为例子。
export PATH=/Users/lemon/Library/Python/3.6/bin 
```

## 开始创建工程

现在，您可以开始准备开发 ESP32 应用程序了。您可以从 ESP-IDF 中 [examples](https://github.com/espressif/esp-idf/tree/ad3b820e7/examples) 目录下的 [get-started/hello_world](https://github.com/espressif/esp-idf/tree/ad3b820e7/examples/get-started/hello_world) 工程开始。

将 [get-started/hello_world](https://github.com/espressif/esp-idf/tree/ad3b820e7/examples/get-started/hello_world) 复制至您本地的 `~/esp` 目录下：

### Linux 和 MacOS 操作系统

```shell
cd ~/esp
cp -r $IDF_PATH/examples/get-started/hello_world .
```

### Windows 操作系统

```shell
cd %userprofile%\esp
xcopy /e /i %IDF_PATH%\examples\get-started\hello_world hello_world
```

ESP-IDF 的 [examples](https://github.com/espressif/esp-idf/tree/ad3b820e7/examples) 目录下有一系列示例工程，都可以按照上面的方法进行创建。您可以按照上述方法复制并运行其中的任何示例，也可以直接编译示例，无需进行复制。

**注意**

ESP-IDF 编译系统不支持带有空格的路径。

## 连接设备

现在，请将您的 ESP32 开发板连接到 PC，并查看开发板使用的串口。

通常，串口在不同操作系统下显示的名称有所不同：

- **Windows 操作系统：** `COM1` 等
- **Linux 操作系统：** 以 `/dev/tty` 开始
- **MacOS 操作系统：** 以 `/dev/cu.` 开始

有关如何查看串口名称的详细信息，请见 [与 ESP32 创建串口连接](ref/serial_driver.md)。

## 配置

请进入第五步：开始创建工程 中提到的 `hello_world` 目录，并运行工程配置工具 `menuconfig`。

### Linux 和 MacOS 操作系统

```
cd ~/esp/hello_world
make menuconfig
```

### Windows 操作系统

```
cd %userprofile%\esp\hello_world
make menuconfig
```

如果之前的步骤都正确，则会显示下面的菜单：

![](img/project-configuration.png)

进入菜单后，选择 `Serial flasher config` > `Default serial port` 配置串口（设备将通过该串口加载工程）。按回车键确认选择，点击 `< Save >` 保存配置，然后点击 `< Exit >` 退出 `menuconfig`。

`menuconfig` 工具的常见操作见下。

- `上下箭头`：移动
- `回车`：进入子菜单
- `ESC 键`：返回上级菜单或退出
- `英文问号`：调出帮助菜单（退出帮助菜单，请按回车键）。
- `空格`、`Y 键``或``N 键`：使能/禁用 `[*]` 配置选项
- `英文问号` ：调出有关高亮选项的帮助菜单
- `/ 键`：寻找配置项目

## 编译和烧录

请使用以下命令，编译烧录工程：

```shell
make flash
```

运行以上命令可以编译应用程序和所有 ESP-IDF 组件，接着生成 bootloader、分区表和应用程序二进制文件。接着，这些二进制文件将被烧录至 ESP32 开发板。

如果一切顺利，可在烧录完成后看到类似下方的打印信息（代表加载进程）。接着，开发板将会复位，应用程序 “hello_world” 开始启动。

```shell
esptool.py v2.0-beta2
Flashing binaries to serial port /dev/ttyUSB0 (app at offset 0x10000)...
esptool.py v2.0-beta2
Connecting........___
Uploading stub...
Running stub...
Stub running...
Changing baud rate to 921600
Changed.
Attaching SPI flash...
Configuring flash size...
Auto-detected Flash size:4MB
Flash params set to 0x0220
Compressed 11616 bytes to 6695...
Wrote 11616 bytes (6695 compressed) at 0x00001000 in 0.1 seconds (effective 920.5 kbit/s)...
Hash of data verified.
Compressed 408096 bytes to 171625...
Wrote 408096 bytes (171625 compressed) at 0x00010000 in 3.9 seconds (effective 847.3 kbit/s)...
Hash of data verified.
Compressed 3072 bytes to 82...
Wrote 3072 bytes (82 compressed) at 0x00008000 in 0.0 seconds (effective 8297.4 kbit/s)...
Hash of data verified.

Leaving...
Hard resetting...
```

如果使用 Eclipse IDE，而非 `make` 编译系统，请参考官方 [Eclipse 指南](https://docs.espressif.com/projects/esp-idf/zh_CN/latest/get-started/eclipse-setup.html)。

## 监视器

使用 `make monitor` 命令，监视 “hello_world” 的运行情况。

运行该命令后，IDF 监视器用程序将启动：

```shell
$ make monitor
MONITOR
--- idf_monitor on /dev/ttyUSB0 115200 ---
--- Quit:Ctrl+] | Menu:Ctrl+T | Help:Ctrl+T followed by Ctrl+H ---
ets Jun  8 2016 00:22:57

rst:0x1 (POWERON_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)
ets Jun  8 2016 00:22:57
...
```

此时，就可以在启动日志和诊断日志之后，看到打印的 “Hello world!” 了。

```shell
...
Hello world!
Restarting in 10 seconds...
I (211) cpu_start:Starting scheduler on APP CPU.
Restarting in 9 seconds...
Restarting in 8 seconds...
Restarting in 7 seconds...
```

**使用快捷键 `Ctrl+]`，退出 IDF 监视器。**

如果 IDF 监视器在烧录后很快发生错误，或打印信息全是乱码（见下），很有可能是因为你的开发板选用了 26 MHz 晶振，而 ESP-IDF 默认支持大多数开发板使用的 40 MHz 晶振。

```
e���)(Xn@�y.!��(�PW+)��Hn9a؅/9�!�t5��P�~�k��e�ea�5�jA
~zY��Y(1�,1�� e���)(Xn@�y.!Dr�zY(�jpi�|�+z5Ymvp
```

此时，按照如下步骤操作：

1. 退出监视器。
2. 打开 [menuconfig](https://docs.espressif.com/projects/esp-idf/zh_CN/latest/get-started/index.html#get-started-configure)，
3. 进入 `Component config` –> `ESP32-specific` –> `Main XTAL frequency` 进行配置，将 [CONFIG_ESP32_XTAL_FREQ_SEL](https://docs.espressif.com/projects/esp-idf/zh_CN/latest/api-reference/kconfig.html#config-esp32-xtal-freq-sel) 设置为 26 MHz。
4. 然后，请重新 [编译和烧录](https://docs.espressif.com/projects/esp-idf/zh_CN/latest/get-started/index.html#get-started-build-and-flash) 应用程序。

注解

也可以运行以下命令，一次性执行构建、烧录和监视过程：

```
make flash monitor
```

此外，请前往 [IDF 监视器](https://docs.espressif.com/projects/esp-idf/zh_CN/latest/api-guides/tools/idf-monitor.html)，了解更多使用 IDF 监视器的快捷键和其他详情。

## 环境变量

用户可以在使用 `make` 命令时 **直接设置** 部分环境变量，而无需进入 `make menuconfig` 进行重新配置。这些变量包括：

| 变量                                                         | 描述与使用方式                             |
| ------------------------------------------------------------ | ------------------------------------------ |
| `ESPPORT`                                                    | 覆盖 `flash` 和 `monitor` 命令使用的串口。 |
| 例：`make flash ESPPORT=/dev/ttyUSB1`, `make monitor ESPPORT=COM1` |                                            |
| `ESPBAUD`                                                    | 覆盖烧录 ESP32 时使用的串口速率。          |
| 例：`make flash ESPBAUD=9600`                                |                                            |
| `MONITORBAUD`                                                | 覆盖监控时使用的串口速率。                 |
| 例：`make monitor MONITORBAUD=9600`                          |                                            |

注解

您可导出环境变量（例：`export ESPPORT=/dev/ttyUSB1`）。 在同一会话窗口中，如果未被同步覆盖，所有 `make` 命令均会使用导出的环境变量值。

## 更新 ESP-IDF

乐鑫会不时推出更新版本的 ESP-IDF，修复 bug 或提出新的特性。因此，在使用时，应注意更新本地的版本。最简单的方法是：直接删除您本地的 `esp-idf` 文件夹，然后按照 [第二步：获取 ESP-IDF](https://docs.espressif.com/projects/esp-idf/zh_CN/latest/get-started/index.html#get-started-get-esp-idf) 中的指示，重新完成克隆。

如果希望将 ESP-IDF 克隆到新的路径下，请务必 [重新设置 IDF_PATH](https://docs.espressif.com/projects/esp-idf/zh_CN/latest/get-started/add-idf_path-to-profile.html)。否则，工具链将无法找到 ESP-IDF。

此外，您可以仅更新变更部分。具体方式，请前往 [更新](https://docs.espressif.com/projects/esp-idf/zh_CN/latest/versions.html#updating) 章节查看。