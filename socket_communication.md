# Socket通信

## 实验任务

socket几乎是整个网络通信的基础，本实验练习Micropython中的Socket模块。

完成以下几个任务：

1. 熟悉socket api 的主要用法，并总结socke编程的主要流程
2. 以ESP32为server, pc 为client， 编写程序实现基本的socket通信。
3. 在ESP32中，编写socket通信程序，实现在线观看星球大战字符动画。

## socket模块 API文档

### 宏

`socket`模块中定义了许多和协议相关的宏，如下表:

| 宏定义名称            | 值（int） | 功能           | 含义          |
| :-------------------- | :-------- | :------------- | :------------ |
| `socket.AF_INET`      | 2         | 地址簇         | TCP/IP – IPv4 |
| `socket.AF_INET`      | 10        | 地址簇         | TCP/IP - IPv6 |
| `socket.SOCK_STREAM`  | 1         | 套接字类型     | TCP流         |
| `socket.SOCK_DGRAM`   | 2         | 套接字类型     | UDP数据报     |
| `socket.SOCK_RAW`     | 3         | 套接字类型     | 原始套接字    |
| `socket.SO_REUSEADDR` | 4         | 套接字类型     | socket可重用  |
| `socket.IPPROTO_TCP`  | 16        | IP协议号       | TCP协议       |
| `socket.IPPROTO_UDP`  | 17        | IP协议号       | UDP协议       |
| `socket.SOL_SOCKET`   | 4095      | 套接字选项级别 |               |

### 函数

#### socket.getaddrinfo(host, port)

函数说明：将主机域名（host）和端口（port）转换为用于创建套接字的5元组序列。元组列表的结构如下:

```
(family, type, proto, canonname, sockaddr)
```

示例：

```
>>> info = socket.getaddrinfo("127.0.0.1", 10000)
>>> print(info)
[(2, 1, 0, '127.0.0.1', ('127.0.0.1', 10000))]
```

#### socket.socket([af, type, proto])

函数说明：创建套接字。

- `af`：地址
- `type`：类型
- `proto`：协议号

**注意： 一般不指定proto参数，因为有些Micropython固件提供默认参数。 **
示例：

```
>>> s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
>>> print(s)
<socket>
```

#### socket.socket.setsockopt(level, optname, value)

函数说明：根据选项值设置套接字。

- `level`：套接字选项级别
- `optname`：套接字的选项
- `value`：可以是一个整数，也可以是一个表示缓冲区的bytes类对象。

示例：

```
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
```

#### socket.socket.bind(address)

函数说明：以列表或元组的方式绑定地址和端口号。

- `address`：一个包含地址和端口号的列表或元组。

示例：

```
addr = ("127.0.0.1",10000)
s.bind(addr)
```

#### socket.socket.listen([backlog])

函数说明：监听套接字，使服务器能够接收连接。

- `backlog`：接受套接字的最大个数，至少为0，如果没有指定，则默认一个合理值。

#### socket.socket.accept()

函数说明：接收连接请求。 
**注意：只能在绑定地址端口号和监听后调用，返回conn和address。**

- conn：新的套接字对象，可以用来收发消息
- address：连接到服务器的客户端地址

示例：

```
conn,addr = s.accept()
```

#### socket.socket.connect(address)

函数说明：连接服务器。

- address：服务器地址和端口号的元组或列表

示例：

```
host = "192.168.3.147"
port = 100
s.connect((host, port))
```

#### socket.socket.send(bytes)

函数说明：发送数据，并返回发送的字节数。

- bytes：bytes类型数据

示例：

```
s.send("hello 1ZLAB, I am TCP Client")
```

#### socket.socket.sendall(bytes)

函数说明：与send(）函数类似，区别是sendall()函数通过数据块连续发送数据。

- bytes：bytes类型数据

示例：

```
s.sendall("hello 1ZLAB, I am TCP Client")
```

#### socket.socket.sendto(bytes, address)

函数说明：发送数据，目标由address决定，用于UDP通信，返回发送的数据大小。

- bytes：bytes类型数据
- address：目标地址和端口号的元组

示例：

```
data = sendto("hello 1ZLAB", ("192.168.3.147", 100))
```

#### socket.socket.recv(bufsize)

函数说明：接收数据，返回接收到的数据对象。

- bufsize：指定一次接收的最大数据量

示例：

```
data = conn.recv(1024)
```

#### socket.socket.recvfrom(bufsize)

函数说明：接收数据，用于UDP通信，并返回接收到的数据对象和对象的地址。

- bufsize：指定一次接收的最大数据量

示例：

```
data,addr=fd.recvfrom(1024)
```

#### socket.socket.settimeout(value)

函数说明：设置超时时间，单位：秒。 
示例：

```
s.settimeout(2)
```

#### socket.socket.readline()

函数说明：接收一行数据，遇换行符结束，并返回接收数据的对象 。

#### socket.socket.write(buf)

函数说明：将字节类型数据写入套接字，并返回写入数据的大小。

#### socket.socket.close()

函数说明：关闭套接字。 
示例：

```
s.close()
```

## TCP服务端和客户端通信示例

确保你的ESP32和你的PC在同一局域网内。

在接下来的示例中，我们以ESP32建立TCP服务端，在PC上编写脚本 创建TCP客户端，与服务器进行通信。

### ESP32 TCP服务端

```python
"""
ESP32 TCP Server
"""

import socket
import network

port = 10000  #端口号
listenSocket = None  #套接字

try:
    # 注意：线连接到WiFi网络！
    # 如果未连接到网络，以下是连接到网络的代码
    # Wifi.connect()
    sta_if = network.WLAN(network.STA_IF); 
    sta_if.active(True)
    sta_if.scan()                             # Scan for available access points
    sta_if.connect("SSID", "password") # Connect to an AP
    sta_if.isconnected()                      # Check for successful connection

    ip = sta_if.ifconfig()[0]   #获取IP地址
    listenSocket = socket.socket()   #创建套接字
    listenSocket.bind((ip, port))   #绑定地址和端口号
    listenSocket.listen(1)   #监听套接字, 最多允许一个连接
    listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   #设置套接字
    print ('tcp waiting...')

    while True:
        print("accepting.....")
        conn, addr = listenSocket.accept()   #接收连接请求，返回收发数据的套接字对象和客户端地址
        print(addr, "connected")

        while True:
            data = conn.recv(1024)   #接收数据（1024字节大小）
            if(len(data) == 0):   #判断客户端是否断开连接
                print("close socket")
                conn.close()   #关闭套接字
                break
            print(data)
            ret = conn.send(data)   #发送数据
except:
    if(listenSocket):   #判断套接字是否为空
        listenSocket.close()   #关闭套接字
```

### PC TCP客户端

```python
# -*- coding: UTF-8 -*-
# PC TCP Client

import socket               								# 导入 socket 模块

s = socket.socket()         								# 创建 socket 对象
host = '<ip of your esp32 tcp server>'      # esp32 ip
port = 10000                								# 设置端口号

s.connect((host, port))

if __name__ == '__main__':
    while True:
        msg = input('>>> ').encode()
        s.send(msg)
```

### 操作流程

1. 将TCP SERVER代码上传至ESP32开发板，并进入REPL模式
2. 将TCP CLINET代码保存到本机，运行 
3. 在>>>提示符后输入任意字符，观察server端是否接受并打印。

下图为操作效果

![](img/socket_communication.png)

## 收看星球大战字符动画

> blinkenlights.nl网站提供的星球大战Asciimation服务。它使用端口23上的telnet协议将数据流式传输给任何连接的人。

### 1 、在pc terminal 体验星球大战动画

在 terminal终端中打开动画，并观察效果

```shell
telent towel.blinkenlights.nl
```

如果你的PC没有安装telnet，请按照如下命令安装

```shell
# for ubuntu
sudo apt-get update
sudo apt-get install telnet
# for mac osx
brew install telnet
```



### 2、在REPL中使用SOCKET实验

接下来，让我们建立一个TCP通信，在我们的REPL中观看星球大战。

将ESP32开发板通过WIFI连接到外网，具体请参见[wifi](wifi_network_connection.md)

导入套接字模块：

```
>>> import socket
```

然后我们通过域名来获取服务器的地址

```
>>> addr_info = socket.getaddrinfo("towel.blinkenlights.nl", 23)
```

`getaddrinfo` 函数实际上返回一个地址列表:

```
[(2, 1, 0, 'towel.blinkenlights.nl', ('94.142.241.111', 23))]
```

我们只需要获取服务器的IP地址和端口，对应于该列表第一项的最后一个元组：

```
>>> addr = addr_info[0][-1]
```

建立一个socket对象，然后使用上面的IP地址和端口号与服务器进行连接：

```
>>> s = socket.socket()
>>> s.connect(addr)
```

现在我们已经连接，我们可以获取并显示数据了：

```
>>> while True:
...     data = s.recv(500)
...     print(str(data, 'utf8'), end='')
...
```

Ctrl-D，执行循环代码，当这个循环执行时，它应该开始显示动画（使用ctrl-C来中断它）。

### 3 、编制程序

请将上述程序编写为模块，在main主模块中调用，并上传至esp32开发板执行。

## 思考

如何使用 Socket通信，来远程点亮ESP32控制的LED呢？你将制定何种通信协议呢？