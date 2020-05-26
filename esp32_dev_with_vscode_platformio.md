# VS Code 下使用 PlatformIO 进行IOT应用程序的开发

## 实验准备

- [必读：PlatformIO基础概念以及对ESP32的支持](ref/platformio_introduction.md)
- VS Code 下安装 PlatformIO插件
- [arduino语法手册](http://images.shoring.vip/2017/10/3517486698.pdf)

## PlatformIO开发环境简介

### home

![image-20200526134607394](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf5sx7r44ij31400tbai0.jpg)



### 工程管理

![image-20200526134718061](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf5syfpyqgj31400if76m.jpg)



### 库管理

PlatformIO提供了丰富的代码库，包括内建库和第三方库，给开发者提供了丰富的代码支持和参考。

![image-20200526135015504](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf5t1io5knj30xf0u07b1.jpg)



### 开发板管理

PlatformIO内建800+开发板，并提供客户定制开发板功能。

![image-20200526135148899](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf5t34tnj2j314b0t6dlj.jpg)



### 开发框架Platform,framework的管理

PlatformIO提供Platform的管理功能，可以安装，升级，卸载芯片平台架构。平台架构包含，嵌入式，桌面式。同时对于各种平台提供了相应的开发框架framework的功能。

![image-20200526135654331](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf5t8fsnswj314b0rxjw7.jpg)



![image-20200526135747429](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf5t9ckwhbj30wz0u0wk6.jpg)



### 设备管理

主要是对开发机器串口，存储器以及网络设备提供管理功能：

![image-20200526135938953](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf5tbad8suj314b0i90v4.jpg)

PlatformIO 包含两个framework 用以支持 NodeMCU32开发：

- ESP-IDF
- Arduino

以下分别对两种方式进行实验。

## VS Code + ESP-IDF

### 创建工程

进入PlatformIO HOME, CREATE NEW PROJECT:

![image-20200526132621878](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf5scni8ycj316f0u0n4q.jpg)



在Wizard中搜索开发板nodemcu32s, 并选择软件开发框架framework为ESP-IDF，命名项目，选择工程路径（Location）。

![image-20200526133543563](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf5sme5m6tj30jz0fmmyc.jpg)

创建过程中会**自动的下载相关的编译工具链，开发框架framework, SDK，以及芯片架构platform**等。如果希望自行安装，可按照下图方式进行，建议用wizard。

![image-20200526142105261](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf5txl7xa9j30u80jbaf2.jpg)

完成后会自动生成如下图结构的代码包：

![image-20200526142141348](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf5ty7ujo5j31240kcjzk.jpg)

其中：

- .pio是platformIO的配置文件，该文件自动生成
- Include文件夹是包含文件
- Lib是库文件夹
- test是编译测试文件夹
- **src是源文件夹**

SRC就是我们需要编写源代码的文件夹，ESP-IDF官方文件支持C语言。

### 编写代码

打开main.c文件，该文件是自动生产的，是程序的入口。添加如下代码覆盖的该文件。

```c
#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "driver/gpio.h"
#include "sdkconfig.h"

/* Can use project configuration menu (idf.py menuconfig) to choose the GPIO to blink,
   or you can edit the following line and set a number here.
*/
// #define BLINK_GPIO CONFIG_BLINK_GPIO
#define BLINK_GPIO 2

void app_main(void)
{
    /* Configure the IOMUX register for pad BLINK_GPIO (some pads are
       muxed to GPIO on reset already, but some default to other
       functions and need to be switched to GPIO. Consult the
       Technical Reference for a list of pads and their default
       functions.)
    */
    gpio_pad_select_gpio(BLINK_GPIO);
    /* Set the GPIO as a push/pull output */
    gpio_set_direction(BLINK_GPIO, GPIO_MODE_OUTPUT);
    while(1) {
        /* Blink off (output low) */
	printf("Turning off the LED\n");
        gpio_set_level(BLINK_GPIO, 0);
        vTaskDelay(1000 / portTICK_PERIOD_MS);
        /* Blink on (output high) */
	printf("Turning on the LED\n");
        gpio_set_level(BLINK_GPIO, 1);
        vTaskDelay(1000 / portTICK_PERIOD_MS);
    }
}

```





### 编译代码

编译代码操作如下图所示：

![image-20200526144414764](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf5uloyk5oj30u00xswp0.jpg)



当一切正常运行时，将会出现如下图所示的编译成功信息。

![image-20200526144747870](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf5upduzgkj30sj0sn46a.jpg)



### 上传固件到开发板

首先需要确保开发板与计算机正确连接和配置，进入到工程，开启**配置**

![image-20200526145746650](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf5uzrw9vlj30wn0p742f.jpg)

在工程配置中，分别在UPLOAD配置与MONITOR配置中配置正确的串口参数，即串口设备号，以及波特率：

![image-20200526145948195](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf5v1vs38ej30u00zy0xl.jpg)



接下来即可上传固件，并运行固件并在串口中监视调试固件了。

上传如下图：

![image-20200526150629272](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf5v8tvdmaj30u00z2487.jpg)



### 监视串口与调试

运行程序后，可按照下图监视串口输出：

![image-20200526150856165](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf5vbdnb3ej30u00z2gvg.jpg)



NODEMCU-32S需要专用的调试器（DEBUGGER），因此在本实验中不具体演示。

## VS Code + Arduino

使用Arduino开发的过程与ESP-IDF基本一致，只是在配置framework和代码编写上略有区别，以下只写不同的部分，其他请参照上节的ESP-IDF的过程。

### 工程配置

在工程配置中，或是在创建工程中选择framework为：arduino

![image-20200526151808370](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf5vky75d2j30wr0nwadi.jpg)



### 代码编写

arduino生成的代码文件结构如下图：

![image-20200526152057034](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf5vnw0la3j309h08374q.jpg)



同理，源代码在SRC文件夹下存储。

请将如下代码替换到main.cpp， 

```cpp
#include <Arduino.h>

void setup()
{
  // put your setup code here, to run once:
  Serial.begin(115200);
  int ledPin = 2;
  pinMode(ledPin, OUTPUT);
}

void loop()
{
  // put your main code here, to run repeatedly:
  // Serial.println("hello world");
  // delay(1000);
  int ledPin = 2;
  digitalWrite(ledPin, HIGH);
  delay(1000);
  digitalWrite(ledPin, LOW);
  delay(1000);
}
```





### 编译，上传，监视

操作同ESP-IDF下。

## 思考

以上讲述和练习了如何在platformIO下进行如下所列的开发步骤：

- 创建工程
- 编写代码
- 编译
- 固件上传
- 监视输出

如果，修改了程序后，需要如下操作，请各位自行思考并操作：

- 清空编译结果并重新编译
- 擦除闪存

请参照示例程序，尝试在ESP-IDF或arduino下实现之前用micropython实现的功能。



