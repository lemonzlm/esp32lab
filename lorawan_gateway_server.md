# LoRaWAN 网关及服务器搭建

## LoRaWAN 服务器

### 要求

1. 拥有公网 IP 服务器
2. Linux 操作系统 (Ubuntu、Debian等)

----

### 部署 Docker

以 Ubuntu 为例，使用 apt 软件包管理

```shell
apt-get update
apt-get install docker
```

#### 更换 Docker 镜像源

1. 在 [阿里云申请镜像加速器](https://cr.console.aliyun.com) 申请镜像加速器
2. 获得加速地址 `https://xxxxxx.mirror.aliyuncs.com`
3. 执行以下指令，将地址修改成你获取的

```shell
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://xxxxxx.mirror.aliyuncs.com"]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker
```

---

### 部署 ChirpStack 组件

下载 Docker Compose 配置

```shell
wget https://raw.githubusercontent.com/brocaar/chirpstack-docker/master/docker-compose-env.yml
```

打开文件进行容器相关配置

完成配置后，即可执行以下指令部署

```shell
docker-compose up
```

浏览 http://localhost:8080 即可访问 Application Server

初始用户密码为`admin`

---

### 配置ChirpStack组件

#### 创建网络服务

1. 点击 Network-server，创建
2. 输入服务器名字与地址

> 本教程将根据Docker容器名填写：chirpstack-network-server:8000

#### 创建网关预设配置

1. 点击 Gateway-profiles，创建
2. 填写网关名字
3. 填写统计间隙（默认填30s即可）
4. 填写信道

> CN470 信道填写：0, 1, 2, 3, 4, 5, 6, 7

#### 创建服务预设配置

1. 点击 Service-profiles，创建
2. 填写名字
3. 设置最大/最小允许 Data-Rate

> CN470 DR 填写：最小0 最大5

#### 创建设备预设配置

1. 点击 Device-profiles，创建
2. 填写名字
3. 根据设备的 LoRaWAN 版本选择 MAC 版本
4. 如果设备支持 Class-B 或 Class-C，勾选并配置参数

#### 添加网关

1. 点击 Gateway，创建
2. 填写网关名字，网关 ID
3. 选择网络服务器 (Network-server)
4. 选择网关配置 (Gateway-profile)

#### 创建应用

1. 点击 Application，创建
2. 填写应用名字
3. 选择 Service-profiles

> Profiles 均选择自己创建的即可

#### 添加设备

1. 选择应用，点击添加设备
2. 填写设备名字、EUI、Device-profiles
3. 创建成功后，点击设备 Keys 或 Activation 标签
4. 点击随机生成密钥，并对设备程序进行密钥配置

> 生成的密钥将用于设备激活，设备程序中使用的密钥必须与服务器配置的一致才能顺利入网

---

## LoRaWAN 网关

### 要求

1. 树莓派 (Raspberry Pi 3)
2. 树莓派兼容 LoRa 网关模块 [(RAK 2245)](https://docs.rakwireless.com/Product-Categories/WisLink/RAK2245-Pi-HAT/Overview/)

---

### 刷入固件

1. 下载 RAK 模块官方树莓派固件 [(固件下载)](https://downloads.rakwireless.com/LoRa/RAK2245-Pi-HAT/Firmware/RAK2245_Latest_Firmware.zip)
2. 使用 [balenaEtcher](https://www.balena.io/etcher/) 烧录固件至 SD 卡上

---

### 配置 LoRaWAN网关

#### 连接树莓派

成功刷入固件后，将 SD 卡、网关模块、模块天线安装在树莓派上，通电开机。在稍等片刻后，可通过电脑 Wi-Fi 搜索到SSID为 `Rakwireless_XXXX` 的接入点，密码为  `rakwireless ` ，默认树莓派 IP 地址为 `192.168.230.1`

#### 登录树莓派

使用电脑 ssh 登录至树莓派，默认密码为 `raspberry`

```shell
ssh pi@192.168.230.1
```

#### 配置网关网络

输入以下指令打开配置界面

```shell
sudo gateway-config
```

以下为配置界面

![](https://docs.rakwireless.com/assets/images/wislink-lora/rak2245-pi-hat-edition/quickstart/5.accessing-the-internet/config-options.png)

为使用树莓派板载 Wi-Fi 访问网络，选择 **选项5**。默认情况下固件为 AP 模式，为了让树莓派访问 Wi-Fi 网络，需要将其切换为客户端模式，选择 **选项2**。

![](https://docs.rakwireless.com/assets/images/wislink-lora/rak2245-pi-hat-edition/quickstart/5.accessing-the-internet/wifi-config.png)

然后选择 **选项4** 进行设置 WI-FI 接入点 SSID 和密码。

![](https://docs.rakwireless.com/assets/images/wislink-lora/rak2245-pi-hat-edition/quickstart/5.accessing-the-internet/wifi-ssid.png)

![](https://docs.rakwireless.com/assets/images/wislink-lora/rak2245-pi-hat-edition/quickstart/5.accessing-the-internet/set-wifi.png)

![](https://docs.rakwireless.com/assets/images/wislink-lora/rak2245-pi-hat-edition/quickstart/5.accessing-the-internet/set-password.png)

完成配置后输入重启指令重启树莓派即可完成网络配置

```shell
sudo reboot
```

#### 配置网关连接服务器

在配置界面选择 **选项2**，选择 **Server is ChirpStack**

![](https://docs.rakwireless.com/assets/images/wislink-lora/rak2245-pi-hat-edition/quickstart/6.configure-the-gateway/chirpstack.png)

然后选择 **选项1**，配置连接LoRaWAN。首先需要配置网关运行的LoRa频段

> 中国选择 CN470 频段

![](https://docs.rakwireless.com/assets/images/wislink-lora/rak2245-pi-hat-edition/quickstart/6.configure-the-gateway/chirpstack_channel.png)

然后设置 ChirpStack 服务器地址

![](https://docs.rakwireless.com/assets/images/wislink-lora/rak2245-pi-hat-edition/quickstart/6.configure-the-gateway/loraserver_ip.png)

> 默认为本地的 ChirpStack 服务器地址 `127.0.0.1`

配置完成后，等待网关连接成功即可在 ChirpStack 网站上看到网关信息

![](https://docs.rakwireless.com/assets/images/wislink-lora/rak2245-pi-hat-edition/quickstart/8.connecting-to-chirpstack/chirpstack-last-seen.png)

---

## LoRaWAN 节点

### 要求

1. ESP32 (支持Arduino)
2. RAK 811

---

### 刷入网关模块固件

#### 模块组装

1. RXD 和 TXD 跳线切换到 CRX 和 CTX 
2. BOOT 跳线切换到 3V3
3. 使用 USB 线连接到 COM 口上

> 完成刷入固件后需要还原跳线才能正常启动

![](https://github.com/RAKWireless/WisNode-Arduino-Library/raw/master/Documents%20and%20tools/image/Arduino_mode_v1.3.png)

![](https://github.com/RAKWireless/WisNode-Arduino-Library/raw/master/Documents%20and%20tools/image/jump_boot.png)

#### 操作刷入固件

1. 下载 Arduino 兼容固件 [(固件下载)](https://github.com/RAKWireless/WisNode-Arduino-Library/tree/master/Documents%20and%20tools/WisNode-Arduino%20version-Firmware)
2. 打开 [STM32CubeProgrammer](https://www.st.com/zh/development-tools/stm32cubeprog.html)
3. 选择好接口、波特率，点击 Connect

![](https://github.com/RAKWireless/WisNode-Arduino-Library/raw/master/Documents%20and%20tools/image/connect_STM32cubeprogrammer.png)

4. 点击 Open file 选择固件
5. 点击 Download 进行刷入固件

![](https://github.com/RAKWireless/WisNode-Arduino-Library/raw/master/Documents%20and%20tools/image/burn_firmware.png)

---

### 组装模块

1. 将模块 TX、RX、3V3、GND 端口连接至 ESP32 相应接口上
2. ESP32 连接至电脑

---

### 编写节点程序

采用 [WisNode-Arduino-Library](https://github.com/RAKWireless/WisNode-Arduino-Library) 库，参考库自带的例子代码 [JoinNetworkOTAA](https://github.com/RAKWireless/WisNode-Arduino-Library/blob/master/Arduino-RAK811-Library/examples/JoinNetworkOTAA/JoinNetworkOTAA.ino) 编写一个简易程序用于测试 LoRaWAN 连通性，按照以下进行修改

- 修改 DevEui、AppEui (与DevEui相同)，与服务器端设备数据一致
- 修改 AppKey，与服务器端设备激活 OTTA 中的密钥一致
- 修改 TXpin、RXpin 端口数，与实际物理连接端口一致 (查看开发版端口定义)

完成修改后，连接设备、编译程序、下载程序。通过调试端口可看到程序运行情况，通过 ChirpStack 设备数据日志可看到节点上传至服务器的数据

> 测试时需要先配置启动 LoRaWAN 网关与服务器，节点才能正常工作

![](https://github.com/RAKWireless/WisNode-Arduino-Library/raw/master/Documents%20and%20tools/image/LoRaWAN_log.png)

