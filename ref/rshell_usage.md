# Rshell 操作手册

rshell也称为远程mciropython shell。专门针对MicroPython的远程shell，基于串口和网络。支持多种模式：

- raw REPL
- 远程文件管理
  - 复制本地文件到目标板
  - 在远程目标板进行文件系统常规操作，如目录管理，文件管理等
- 调试

Rshell在主机上运行，可以将MicroPython代码发送到目标板文件系统下（如pyboard，我们的实验中是esp32开发版，也叫nodeMCU-32S），以及从MicroPython的文件系统复制文件。

RSHELL可以进入常规REPL，因此rshell也可以用作终端模拟器。

**注意，注意，注意** ！使用这些命令时，/flash目录和/sdcard目录（如果插入了SD卡）被认为是在pyboard上，所有其他目录都被认为是在主机上。 对于基于ESP的电路板，您只能使用电路板名称来引用其目录，**在我们的开发版上为为 /pyboard。**

下面我们将详细讲解。

## 安装

```shell
sudo pip3 install rshell
```

## 获取帮助

```shell
$ rshell --help
usage: rshell [options] [command]

Remote Shell for a MicroPython board.

positional arguments:
  cmd                   Optional command to execute

optional arguments:
  -h, --help            show this help message and exit
  -b BAUD, --baud BAUD  Set the baudrate used (default = 115200)
  --buffer-size BUFFER_SIZE
                        Set the buffer size used for transfers (default = 512
                        for USB, 32 for UART)
  -p PORT, --port PORT  Set the serial port to use (default
                        '/dev/cu.SLAB_USBtoUART')
  -u USER, --user USER  Set username to use (default 'micro')
  -w PASSWORD, --password PASSWORD
                        Set password to use (default 'python')
  -e EDITOR, --editor EDITOR
                        Set the editor to use (default 'vi')
  -f FILENAME, --file FILENAME
                        Specifies a file of commands to process.
  -d, --debug           Enable debug features
  -n, --nocolor         Turn off colorized output
  -l, --list            Display serial ports
  -a, --ascii           ASCII encode binary files for transfer
  --wait WAIT           Seconds to wait for serial port
  --timing              Print timing information about each command
  -V, --version         Reports the version and exits.
  --quiet               Turns off some output (useful for testing)

You can specify the default serial port using the RSHELL_PORT environment
variable.
```

## 进入工具命令行

```
rshell
```

进入命令后，可以看到如下提示：

```shell
Using buffer-size of 32
Connecting to /dev/cu.SLAB_USBtoUART (buffer-size 32)...
Trying to connect to REPL  connected
Testing if ubinascii.unhexlify exists ... Y
Retrieving root directories ... /boot.py/ /main.py/ /wifiAccess.py/ /wifiAp.py/
Setting time ... May 04, 2019 17:11:40
Evaluating board_name ... pyboard
Retrieving time epoch ... Jan 01, 2000
Welcome to rshell. Use Control-D (or the exit command) to exit rshell.
/Users/lemon/esp>
```

## 查看支持的命令

```shell
/Users/lemon/esp> help

Documented commands (type help <topic>):
========================================
args    cat  connect  echo  exit      filetype  ls     repl  rsync
boards  cd   cp       edit  filesize  help      mkdir  rm    shell

Use Control-D (or the exit command) to exit rshell.
```

## 查看命令用法

```shell
/Users/lemon/esp> help repl
repl [board-name] [~ line [~]]

Enters into the regular REPL with the MicroPython board.
Use Control-X to exit REPL mode and return the shell. It may take
a second or two before the REPL exits.

If you provide a line to the REPL command, then that will be executed.
If you want the REPL to exit, end the line with the ~ character.
```



## 列出本地机器目录文件及文件夹

```shell
/Users/lemon/esp> ls
esp-idf/
firmware/
project/
webrepl/
xtensa-esp32-elf/
xtensa-esp32-elf-osx-1.22.0-80-g6c4433a-5.2.0.tar.gz
```

## 列出目标开发版文件及目录

```shell
# 检查目标板名称
/Users/lemon/esp> boards
pyboard @ pyboard connected Epoch: 2000 Dirs: /boot.py /main.py /wifiAccess.py /wifiAp.py /pyboard/boot.py /pyboard/main.py /pyboard/wifiAccess.py /pyboard/wifiAp.py
# 列出目标版根目录文件
/Users/lemon/esp> ls /pyboard
boot.py       main.py       wifiAccess.py wifiAp.py
```

## 向目标版传输文件

```shell
# 从本机当前目录的test目录下拷贝test.py文件到目标版的根目录下
cp test/test.py /pyboard/
```

## 删除目标版文件

```shell
rm /pyboard/test.py
```

## 编辑目标版文件

```shell
edit /pyboard/test.py
```

**尽管**可以直接编辑目标版文件，我们只有在小的改动时，才这样做。一般情况下是在编辑器编辑好后再上传到目标版。比如`cp`命令。

### 进入到REPL

```
repl

Entering REPL. Use Control-X to exit.
>
MicroPython v1.10-298-g47e76b527 on 2019-04-18; ESP32 module with ESP32
Type "help()" for more information.
>>>
>>>
```



## 参考文档

https://github.com/dhylands/rshell