# **VS Code 下使用 RT-Thread Extension 开发项目**

**本实验为选做，在实际使用中，推荐使用该方法作为代码编写工具，烧录和调试建议使用rshell。**

## 介绍

VSCode 最好用的 MicroPython 插件，为 MicroPython 开发提供了强大的开发环境，主要特性如下：

- 设备快速连接（串口、网络、USB）
- 支持基于 MicroPython 的代码智能补全与语法检查
- 支持 MicroPython REPL 交互环境
- 提供丰富的代码示例与 demo 程序
- 提供工程同步功能
- 支持下载单个文件或文件夹至开发板
- 支持在内存中快速运行代码文件功能
- 支持运行代码片段功能
- 支持多款主流 MicroPython 开发板
- 支持 Windows、Ubuntu、Mac 操作系统

## 开发板支持列表

| 编号 | 开发板名称                                                                                                                                              | 固件获取方式                                                                                                        |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| 1    | [潘多拉 IoT Board 物联网开发板 STM32L475](https://item.taobao.com/item.htm?spm=a1z10.5-c-s.w4002-18400369818.12.2ba47ea5PzJxZx&id=583843059625)         | [RT-Thread 论坛固件汇总贴](https://www.rt-thread.org/qa/forum.php?mod=viewthread&tid=12305&page=1&extra=#pid52954)  |
| 2    | [正点原子 W601 WIFI 物联网开发板](https://item.taobao.com/item.htm?spm=a230r.1.14.13.7c5b4a9bS2LYUD&id=602233847745&ns=1&abbucket=17#detail)            | [RT-Thread 论坛固件汇总贴 ](https://www.rt-thread.org/qa/forum.php?mod=viewthread&tid=12305&page=1&extra=#pid52954) |
| 3    | [正点原子探索者 STM32F407 开发板](https://item.taobao.com/item.htm?spm=a1z10.5-c-s.w4002-18400369818.18.569779dc0A3gkT&id=41855882779)                  | [RT-Thread 论坛固件汇总贴](https://www.rt-thread.org/qa/forum.php?mod=viewthread&tid=12305&page=1&extra=#pid52954)  |
| 4    | [RT-Thread 麻雀一号音视频开发板](https://item.taobao.com/item.htm?spm=a1z0k.7385961.1997985097.d4918997.42d74829w5rUfo&id=606684373403&_u=t2dmg8j26111) | [RT-Thread 论坛固件汇总贴](https://www.rt-thread.org/qa/forum.php?mod=viewthread&tid=12305&page=1&extra=#pid52954)  |
| 5    | [ESP8266](http://docs.micropython.org/en/latest/esp8266/quickref.html)                                                                                  | [官方下载链接](https://micropython.org/download#esp8266)                                                            |
| 6    | [ESP32](http://docs.micropython.org/en/latest/esp32/quickref.html)                                                                                      | [官方下载链接](https://micropython.org/download#esp32)                                                              |
| 7    | [PYboard](http://docs.micropython.org/en/latest/pyboard/quickref.html)                                                                                  | [官方下载链接](https://micropython.org/download#pyboard)                                                            |
| 8    | [others](https://micropython.org/download#other)                                                                                                        | [官方下载链接](https://micropython.org/download#other)                                                              |

编号为 1 - 4 的开发板的固件由 RT-Thread 官方提供，同时针对 MicroPython 插件开发环境进行 **深度优化** ，提供强大的工程同步功能以及更加丰富的固件功能。

## 准备工作

1. 在 windows 操作系统下使用插件需要将 vscode 的默认终端修改为 powershell，如下图所示：

   ![01_select_powershell](https://oss-club.rt-thread.org/uploads/20210508/35dbdbecd0c62d645f9a76bebce0920f.gif)

如果想要使用 MicroPython 自动补全功能（如果暂时不需要自动补全功能，可以跳过后续步骤），还需要进行如下操作：

1. 安装 Python 插件

2. 按照 Python 插件的提示在 PC 上安装 Python3 并加入到系统环境变量中

   ![02_Python plug](https://oss-club.rt-thread.org/uploads/20210508/333fdc4c024cc705ecc90783e377e353.png)

如果在 PC 上已经安装过上述插件和程序，可以跳过此准备步骤。

### Ubuntu 支持

本插件支持在 **ubuntu 18.04** 版本下运行，为了避免在 ubuntu 系统下频繁获取串口权限，需要将当前用户加入到 `dialout` 用户组中，手动输入如下命令即可，`$USERNAME` 是系统当前用户名：

```
sudo usermod -aG dialout $USERNAME
```

注意：配置修改后需要 **重启一下操作系统** 使配置生效。

### Mac 支持

RT-Thread MicroPython 插件支持 Mac 10.15 Catalina 操作系统，直接搜索插件安装即可。

## 快速上手

### 创建 MicroPython 工程

MicroPython 开发的第一步是创建 MicroPython 工程，后续所有操作都必须在工程内才能运行。创建一个新的 MicroPython 工程有两种方式，分别是创建一个空白工程和基于 Demo 创建工程，下面展示这两种方式。

#### 创建一个空白 MicroPython 工程

![03_create_blank_dir](https://oss-club.rt-thread.org/uploads/20210508/950d7dea11702fcf6e5dd2b9890e7a4c.gif)

#### 创建一个基于 Demo 的 MicroPython 工程

通过该功能可以创建一个基于 demo 的 MicroPython 工程，开发者可以直接运行该 Demo 工程或者在该 Demo 的基础上实现自己想要的功能。

![04_create_demo_dir](https://oss-club.rt-thread.org/uploads/20210508/879eb964a6b92e101c9f0f2b49edfbb6.gif)

#### Weather Show Demo 在开发板上的运行效果

![05_demo_express](https://oss-club.rt-thread.org/uploads/20210508/01314f6e06c1e8cfa44b9911442aacaa.png)

### 连接开发板

点击左下角的连接按钮，然后在弹出的设备列表中选择想要连接的设备，即可连接 MicroPython 开发板。

![06_uart_connect](https://oss-club.rt-thread.org/uploads/20210508/83fadd402f18ad1b1a3d3dc65b498620.gif)

### 查看示例代码文件

MicroPython 插件提供丰富的示例代码，可在左侧活动栏中查看示例代码和库文件。右键点击示例文件，在下拉菜单中可以将示例文件添加到工程中。

![07_check_example](https://oss-club.rt-thread.org/uploads/20210508/072cea45db8a8ee5ebea3195130318a8.png)

### 直接在开发板上运行 MicroPython 文件（调试神器）

该功能用于快速调试单个文件，频繁应用在调试代码的过程中。当我们在一个单独的文件中编写测试程序时，使用该功能可以将当前 python 文件下载到开发板的内存中运行，达到快速调试的效果，还可以使用快捷键 `alt + q` 来触发该功能。

![08_direct_run_files](https://oss-club.rt-thread.org/uploads/20210508/bfeb64c05d440f9850e49b8cbe606032.gif)

### 在开发板上运行 MicroPython 代码片段

如果只是想进行代码量不大的代码调试，而不想将文件下载到开发板上，那么可以使用 **代码片段** 功能。在编辑器中选中想要运行的代码片段，然后在右键下拉菜单中选择 `在设备上执行选中的 MicroPython 代码` 选项，即可在 REPL 环境中运行所选代码。

![09_run_code_snippet](https://oss-club.rt-thread.org/uploads/20210508/14e1a5c8509ddce884b3bbdafa42d757.gif)

### 下载文件/文件夹到开发板

如果想要下载单个文件/文件夹到开发板，此时可以使用 **下载单个文件/文件夹到开发板** 的功能。在工程中选中想要下载到开发板上的文件/文件夹，在下拉菜单中使用该功能即可。这里需要注意的是，如果开发板上有同名的文件/文件夹，下载操作将会覆盖这些已有的文件/文件夹。

通过在 `repl` 中输入 `os.listdir()` 命令可以查看相应的文件/文件夹是否下载成功，同样在 `repl` 中还可以使用相应的命令 **删除文件或文件夹**，命令列表如下所示：

| 功能       | 命令                       |
| ---------- | -------------------------- |
| 删除文件   | `os.remove("file_to_del")` |
| 删除文件夹 | `os.rmdir("dir_to_del")`   |

![10_download_file_floder](https://oss-club.rt-thread.org/uploads/20210508/982b0a1c18d9990f5f5f3b64b4c237b5.gif)

### 工程同步功能

点击左下角的同步按钮可以启动工程同步功能。通过该功能可将本地工程中所有目录文件，同步到开发板的文件系统中。该功能推荐在代码调试完成后使用，在调试过程中不必频繁同步工程。

工程同步完成后，可以在 `DEVICE FILES LIST` 栏目中看到 **设备中的文件列表**。

![11_sync_files](https://oss-club.rt-thread.org/uploads/20210508/952968a08e389d66693f29865ab9f8ed.gif)

### 基于 MicroPython 的代码智能补全

本插件支持基于 MicroPython 语法的代码智能补全和语法检查，这一强大功能对于开发 MicroPython 代码十分实用。它可以让开发者在编写函数的同时查看 API 参数提示，同时它给出的醒目提示也让开发者更易于查找代码中的错误。

![12_auto_complete](https://oss-club.rt-thread.org/uploads/20210508/bf264e633145644b4275bce599693422.gif)

## 开发资源

- [RT-Thread MicroPython 开发用户手册](https://www.rt-thread.org/document/site/submodules/micropython/docs/)
- [RT-Thread MicroPython 软件包](https://github.com/RT-Thread-packages/micropython)
- [RT-Thread MicroPython 示例程序及库](https://github.com/RT-Thread/mpy-snippets)
- [RT-Thread MicroPython 论坛](https://www.rt-thread.org/qa/forum.php?mod=forumdisplay&fid=2&filter=typeid&typeid=20)
- [MicroPython IDE 用户指南](https://www.rt-thread.org/document/site/submodules/micropython/docs/MicroPythonPlug-in/MicroPython_IDE_User_Manual/)
- [MicroPython 固件开发指南](https://www.rt-thread.org/document/site/submodules/micropython/docs/MicroPythonPlug-in/MicroPython_Firmware_Development_Guide/)

## 注意事项

- 不要删除工程目录下的 `.mpyproject.json` 文件，该文件是 MicroPython 工程的配置文件，删除后将无法正常运行 MicroPython 代码程序。
