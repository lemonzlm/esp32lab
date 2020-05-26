# PlatformIO基础概念以及对ESP32的支持

## IOT开发平台-PlatformIO

### PlatformIO 是什么

> PlatformIO is an open source ecosystem for IoT development.
>
> Cross-platform IDE and unified debugger.
>
> Remote unit testing and firmware updates.

[PlatformIO](https://platformio.org/) 是一个用于物联网开发的开源生态系统。它提供跨平台的开发环境和统一的调试器，还支持远程单元测试和固件更新。

### PlatformIO 简介

PlatformIO 是**独立于平台**运行的，实际上它只依赖于 python，然而 python 在 macOS、linux 和 windows 都能完美适配. 也就是说 PlatformIO 的工程从一个电脑很容易迁移到另一个电脑，只需要拷贝再使用 PlatformIO 就能完美打开，不管团队中的成员使用什么操作系统 PlatformIO 可以让工程共享变得异常简单。

除此之外, PlatformIO 不仅可以在笔记本和台式机上运行，同样可以运行在**没有显示桌面的服务器**。PlatformIO 的核心(PlatformIO Core) 就是一个终端程序, 它能配合多款IDE协同工作，如：

- 原生插件
  - [VSCode](https://docs.platformio.org/en/latest/integration/ide/vscode.html#ide-vscode)
  - [CLion](https://docs.platformio.org/en/latest/integration/ide/clion.html#ide-clion) (Experimental)

- 云 IDE
  - [Cloud9](https://docs.platformio.org/en/latest/integration/ide/cloud9.html)
  - [Codeanywhere](https://docs.platformio.org/en/latest/integration/ide/codeanywhere.html)
  - [Eclipse Che](https://docs.platformio.org/en/latest/integration/ide/eclipseche.html)
- 桌面 IDE
  - [Atom](https://docs.platformio.org/en/latest/integration/ide/atom.html)
  - [CLion](https://docs.platformio.org/en/latest/integration/ide/clion.html)
  - [CodeBlocks](https://docs.platformio.org/en/latest/integration/ide/codeblocks.html)
  - [Eclipse](https://docs.platformio.org/en/latest/integration/ide/eclipse.html)
  - [Emacs](https://docs.platformio.org/en/latest/integration/ide/emacs.html)
  - [NetBeans](https://docs.platformio.org/en/latest/integration/ide/netbeans.html)
  - [Qt Creator](https://docs.platformio.org/en/latest/integration/ide/qtcreator.html)
  - [Sublime Text](https://docs.platformio.org/en/latest/integration/ide/sublimetext.html)
  - [Vim](https://docs.platformio.org/en/latest/integration/ide/vim.html)
  - [Visual Studio](https://docs.platformio.org/en/latest/integration/ide/visualstudio.html)
  - [VSCode](https://docs.platformio.org/en/latest/integration/ide/vscode.html)

目前官方推荐的 IDE 使用方案就是 VSCode + PlatformIO IDE 插件，界面如下图：

![](https://docs.platformio.org/en/latest/_images/platformio-ide-vscode.png)

- **PIO 统一的调试器**：可以零配置的对支持硬件调试的的嵌入式开发板进行调试工作，调试器支持很多的**架构**和**开发平台**

- 跨平台的代码构建系统，对系统软件没有额外的依赖，硬件支持丰富：

  - 800+ [Boards（开发板）](https://docs.platformio.org/en/latest/boards/index.html#boards)
  - 35+ [Development Platforms（开发平台）](https://docs.platformio.org/en/latest/platforms/index.html#platforms)
  - 20+ [Frameworks（框架）](https://docs.platformio.org/en/latest/frameworks/index.html#frameworks)

  ![](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf5p4f2ekaj30r705hdg7.jpg)

  

- [PIO 远程调试](https://docs.platformio.org/en/latest/plus/pio-remote.html#pioremote)

- [PIO 单元测试](https://docs.platformio.org/en/latest/plus/unit-testing.html#unit-testing)

- C/C++语法自动补全

- C/C++ 智能代码检查，快速专业级开发

- 近8000专业库以及例程

- 多面板，多工程工作流管理

- 串口监测

- 内置终端，自带Platform Core命令行CLI. [PlatformIO Core (CLI)](https://docs.platformio.org/en/latest/core/index.html#piocore) 

- 内建 [PlatformIO Home](https://docs.platformio.org/en/latest/home/index.html#piohome). home中可管理账户，开发板，工程，平台等。

### PlatformIO 解决的问题

- 嵌入式开发的世界让很多人望而却步的主要原因是针对某一个单片机或开发板开发环境配置过程太过复杂：
  - 交叉编译链工具下载、安装和配置
  - 使用厂商独有的 IDE (有时还不是免费的) ，
  - 很多IDE只能支持Windows系统，是的跨平台开发异常不便
- 多个硬件平台 (单片机, 开发板) 需要**不同交叉编译链工具和开发环境**, 需要花费大量精力在配置新的开发环境上
- 为了学习如何使用常规的传感器或执行器件等外设，需要花时间查找合适的库和例程

## PlatformIO 基本概念

PlatformIO 包含几个重要的概念，platform, framewoks,以及boards。platform代表芯片架构，该芯片架构具有相同的指令集，即相同的汇编语言，基于该芯片架构，可以有不同配置的芯片产品，如ST STM32架构都是基于ARM32的位处理器芯片，但是ST的芯片品类极多涵盖了各种场景下的应用，如STMLXXX, STMFXXX等不同型号的芯片。基于同一芯片，供应商可以设计各种类型的开发板，如基于EXPRESS IF的芯片ESP32, 他的开发板的品类非常多，如官方的ESP32-DevkitC，nodeMCU-32S等。

对于每一种Platform，都需要相应的软件架构来支持，应用广泛的芯片架构，往往除了官方的软件架构支持外，还有非常多的第三方软件架构的支持。如：

| Platform  | Framework                        |
| --------- | -------------------------------- |
| Espressif | ESP-IDF, Arduino                 |
| St stm32  | STM32Cube, Arduino, Mbed, Zephyr |

下图以stm32 以及espressif为例说明三者之间的关系：

![image-20200526125846251](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf5rjy34cij30vo0siwib.jpg)



### frameworks（软件架构）

- [Arduino](https://platformio.org/frameworks/arduino)
- [ESP-IDF](https://platformio.org/frameworks/espidf)
- [Mbed](https://platformio.org/frameworks/mbed)
- [STM32Cube](https://platformio.org/frameworks/stm32cube)

### platfom（芯片架构）

- [Espressif 32](https://platformio.org/platforms/espressif32)
- [Espressif 8266](https://platformio.org/platforms/espressif8266)
- [Intel MCS-51 (8051)](https://platformio.org/platforms/intel_mcs51)
- [ST STM32](https://platformio.org/platforms/ststm32)
- [NXP LPC](https://platformio.org/platforms/nxplpc)
- [Nordic nRF51](https://platformio.org/platforms/nordicnrf51)
- [Microchip PIC32](https://platformio.org/platforms/microchippic32)
- [Atmel AVR](https://platformio.org/platforms/atmelavr)

### Boards（开发板）

[nodeMCU-32S](https://docs.platformio.org/en/latest/boards/espressif32/nodemcu-32s.html)

- platform: 		expressif 32
- Framework:     arduino , esp-idf

![](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf5pupq9txj30vw06njse.jpg)

[Discvo L475VG IOT01A](https://docs.platformio.org/en/latest/boards/ststm32/disco_l475vg_iot01a.html)

- platform: 		ST STM32

- Framework:     arduino, STM32Cube, Mbed, Zephyr

  

![](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf5ptmz0aqj30w509u767.jpg)

## PlatformIO 对 ESP32的支持

PlatformIO中，对ESP32的支持非常丰富，共[73](https://platformio.org:443/boards?count=1000&filter%5Bframeworks%5D=espidf&filter%5Bplatform%5D=espressif32&page=1&sorting%5Bname%5D=asc) 种，Platform有1种，framework 共4 种，主流的有两种，包括：

- ESP-IDF
- Arduino