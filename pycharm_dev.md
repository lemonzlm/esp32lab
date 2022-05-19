# Pychar 环境下 Mciropython 的开发配置

PyCharm 是 [JetBrains](https://www.jetbrains.com/) 推出的专业级 Python IDE。Microduino 即将推出支持 [Micropython](http://micropython.org/) 的 ESP32 核心，本文介绍如何在 pycharm 下配置 microPython 开发环境

## 重要提示

本节需要先理解并熟练使用 [rshell](ref/rshell_usage.md)

## 前置条件

### 1. 确认 Python 环境为 3.5 以上版本

```shell
python3 --version
# 如果版本太低，请升级版本
sudo apt-get update
sudo apt-get upgrade python3
# 如果系统没有安装python3，请执行以下操作安装
sudo apt-get install python3
```

### 2. 下载安装 Pycharm 以及 micro python 插件

Pycharm 有商业版本也有社区的开源版本，这里我们使用开源的社区版本（community）。[下载地址在此](https://www.jetbrains.com/pycharm/download)

进入设置页面找到“插件”标签。找名为“micropython”的插件，然后安装。

![安装micropython插件](https://tva1.sinaimg.cn/large/e6c9d24egy1h2dzlbrlmqj216s0u0n11.jpg)

安装完插件后，需要重启 Pycharm 生效。

## 创建 micropython 项目

### 1. 配置开发环境的 python 版本

如下图所示，创建新的项目，注意，新项目使用独立的虚拟环境，your-esp-dir 指你的 Python 代码所在目录。基础解释器可自行选择，推荐选用较新的。

![](https://tva1.sinaimg.cn/large/e6c9d24egy1h2e0m13bpcj20zb0u0jt5.jpg)

### 2. 配置 micropython

在设置中配置我们的开发板和串口。注意，ESP8266 与 ESP32 兼容。Device Path 最好些如你的串口实际地址，如：

```
/dev/ttyUSB0
```

点击确定。

![](https://tva1.sinaimg.cn/large/e6c9d24egy1h2e0lm1ow8j216r0u0400.jpg)

## 代码编写

回到项目中，第一次编写代码时，IDE 会自动检查 micropython 所依赖的包是否应齐备，如果不齐备，会出现如下图所示的界面：

![](https://tva1.sinaimg.cn/large/e6c9d24egy1h2e0jpuj5kj21c60tcn0f.jpg)

点击：上图中的“Missing required Micropython packages”会自动安装所需要的依赖。

当上图的提示消失后，表示已经安装好后，进入如下图所示当前 Python 环境解释器页面检查，看是否有新的包安装。

![](https://tva1.sinaimg.cn/large/e6c9d24egy1h2e0s9ufizj216r0u0n06.jpg)

一般情况，下所需要的依赖包会自动安装。

新建文件，并编写代码，可以看到 Pycharm 的自动补齐是目前 MICROPYTHON 的 IDE 里面做的最好的，因此，强烈建议使用 pycharm 作为代码编辑器。

## 进入 REPL

pycharm 同样可以进入到 repl 模式，如下图：

![](https://tva1.sinaimg.cn/large/e6c9d24egy1h2e0um0k17j20wy0k6tb5.jpg)

当执行完命令后会看到如下的 repl 解释环境

![repL 环境](img/pycharm_repl_interaction.png)

## 安装 rshell

进入如下图所示当前 Python 环境解释器页面，点击+号，进入包安装界面

![](https://tva1.sinaimg.cn/large/e6c9d24egy1h2e0xzogy1j218b0u0whm.jpg)

在包安装页面，搜索 rshell, 并安装。

![](https://tva1.sinaimg.cn/large/e6c9d24egy1h2e108fuv0j21160u0ju3.jpg)

## 使用 [RSHELL](ref/rshell_usage.md) 管理目标版

可以烧录制定文件到目标版，在要烧录的文件编辑窗口点击右键，在下拉菜单下点击"run flash xxx.py"操作如下图。

![烧录文件](img/pycharm_flash_file.png)

**如果实际环境配置不当，该方法可能不会成功。推荐使用 rshell 来烧录文件以及进入 REPL。**

### 1. 新建终端并进入 rshell

![](https://tva1.sinaimg.cn/large/e6c9d24egy1h2e1caec21j210w0u0ju9.jpg)

### 2. 烧录文件

拷贝本地文件到目标版，如 main.py

```shell
cp main.py /pyboard/
```

可见，该方法和菜单下点击"run flash xxx.py"操作是一样的效果，且效率更高。

### 3. 删除文件

```
# 如要删除掉main.py文件
rm /pyboard/main.py
```

### 4. 进入 repl 进行调试

```
repl
# 退出按ctrl+x
```

### 总结

实际使用中，代码编写使用 pycharm，而管理目标版，包括烧录文件，删除文件以及进入 REPL 等操作，推荐使用[rshell](ref/rshell_usage.md)。

|              |                              |
| ------------ | ---------------------------- |
| 编辑器       | Pycharm + micropython plugin |
| Repl         | Rshell                       |
| 文件烧录管理 | Rshell                       |

下图为综合使用的效果：

![use pycharm with rshell](img/pycharm_with_rshell.png)
