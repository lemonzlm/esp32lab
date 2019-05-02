# 实验四：基础开发调试

## REPL:命令行交互解释开发

在上一章，我们学习和使用了在[交互式解释环境](repl_interaction.md)下的开发，可见，在交互式解释环境下，对于代码长的程序，调试起来非常的不方便，即便是REPL提供了批量执行的代码粘贴模式，但是使用也极其不方便。

因此，在实际环境下，REPL只是在测试和熟悉环境下才会使用，而在开发，调试阶段必须要采用其他更为快捷和方便的方法与工具。

因为esp32系列芯片还在不断发展之中，尽管这些年，各方组织包括开源贡献者都为ESP32提供了很多的开发工具，但是各种工具都有一定的不完善以及功能的滞后，下面列出几种常见的esp32开发平台的组合：

- 代码编辑器+ampy
- 代码编辑器+rshell
- 第三方定制的IDE
  - thony
- 基于VS code的 platform IO

常见的代码编辑器有如下几种：

- VS code （c, python, Arduino）
- Sublime (c, python, Arduino)
- Pycharm (python)

**本章前部分以micro python为主要开发语言与环境，因此一下内容中使用`parcharm`  作为默认的代码编辑器**

本手册后部分使用`c语言` 的内容时，我们将编辑器切换为 `vs code`。

## Pycharm 与ampy 

## pycharm 与 rshell



## 定制IDE

