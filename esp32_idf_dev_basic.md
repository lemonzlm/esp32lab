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
mkdir -p ~/esp32
cd ~/esp32
wget https://dl.espressif.com/dl/xtensa-esp32-elf-linux64-1.22.0-80-g6c4433a-5.2.0.tar.gz
tar -xzf xtensa-esp32-elf-linux64-1.22.0-80-g6c4433a-5.2.0.tar.gz
# setup evn
echo 'export PATH="$HOME/esp32/xtensa-esp32-elf/bin:$PATH"' >> ~/.bashrc
```

### 获取ESP-IDF

```shell
mkdir esp32
cd esp32
git clone --recursive https://github.com/espressif/esp-idf.git
```

### 配置环境变量

```shell
## for mac osx
nano ~/.bash_profile
## addlines to the file
export IDF_PATH=~/esp32/esp-idf
## for ubuntu or debian
echo 'export IDF_PATH=$HOME/esp32/esp-idf'>> ~/.bashrc
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