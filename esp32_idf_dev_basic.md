# ESP-IDF 寮€鍙戝熀鏈繃绋�

## 閰嶇疆ESP-IDF

### 鑾峰彇宸ュ叿閾剧殑渚濊禆鍖�

```shell
# for debian or ubuntu
sudo apt-get install gcc git wget make libncurses-dev flex bison gperf python python-pip python-setuptools python-serial python-cryptography python-future python-pyparsing
```

### 鑾峰彇宸ュ叿閾�

```shell
# dowload tool chain
mkdir -p ~/esp
cd ~/esp
wget https://dl.espressif.com/dl/xtensa-esp32-elf-linux64-1.22.0-80-g6c4433a-5.2.0.tar.gz
tar -xzf xtensa-esp32-elf-linux64-1.22.0-80-g6c4433a-5.2.0.tar.gz
# setup evn
echo 'export PATH="$HOME/esp32/xtensa-esp32-elf/bin:$PATH"' >> ~/.bashrc
```

### 鑾峰彇ESP-IDF

```shell
mkdir esp
cd esp
git clone --recursive https://github.com/espressif/esp-idf.git
```

### 閰嶇疆鐜鍙橀噺

```shell
## for mac osx
nano ~/.bash_profile
## addlines to the file
export IDF_PATH=~/esp/esp-idf
## for ubuntu or debian
echo 'export IDF_PATH=$HOME/esp/esp-idf'>> ~/.bashrc
```

### 瀹夎Python杞欢鍖�

```shell
# esp 宸ョ▼榛樿浣跨敤python2
python -m pip install --user -r $IDF_PATH/requirements.txt

## 瀵逛簬python3
pip3 install --upgrade pip
python3 -m pip install --user -r $IDF_PATH/requirements.txt
## 瀵逛簬鏈夌殑绯荤粺锛屽彲鑳借娣诲姞Python鍖呯殑鐜鍙橀噺,浠ユ垜鐨勪负渚嬪瓙銆�
export PATH=/Users/lemon/Library/Python/3.6/bin 
```

## 寮€濮嬪垱寤哄伐绋�

鐜板湪锛屾偍鍙互寮€濮嬪噯澶囧紑鍙� ESP32 搴旂敤绋嬪簭浜嗐€傛偍鍙互浠� ESP-IDF 涓� [examples](https://github.com/espressif/esp-idf/tree/ad3b820e7/examples) 鐩綍涓嬬殑 [get-started/hello_world](https://github.com/espressif/esp-idf/tree/ad3b820e7/examples/get-started/hello_world) 宸ョ▼寮€濮嬨€�

灏� [get-started/hello_world](https://github.com/espressif/esp-idf/tree/ad3b820e7/examples/get-started/hello_world) 澶嶅埗鑷虫偍鏈湴鐨� `~/esp` 鐩綍涓嬶細

### Linux 鍜� MacOS 鎿嶄綔绯荤粺

```shell
cd ~/esp
cp -r $IDF_PATH/examples/get-started/hello_world .
```

### Windows 鎿嶄綔绯荤粺

```shell
cd %userprofile%\esp
xcopy /e /i %IDF_PATH%\examples\get-started\hello_world hello_world
```

ESP-IDF 鐨� [examples](https://github.com/espressif/esp-idf/tree/ad3b820e7/examples) 鐩綍涓嬫湁涓€绯诲垪绀轰緥宸ョ▼锛岄兘鍙互鎸夌収涓婇潰鐨勬柟娉曡繘琛屽垱寤恒€傛偍鍙互鎸夌収涓婅堪鏂规硶澶嶅埗骞惰繍琛屽叾涓殑浠讳綍绀轰緥锛屼篃鍙互鐩存帴缂栬瘧绀轰緥锛屾棤闇€杩涜澶嶅埗銆�

**娉ㄦ剰**

ESP-IDF 缂栬瘧绯荤粺涓嶆敮鎸佸甫鏈夌┖鏍肩殑璺緞銆�

## 杩炴帴璁惧

鐜板湪锛岃灏嗘偍鐨� ESP32 寮€鍙戞澘杩炴帴鍒� PC锛屽苟鏌ョ湅寮€鍙戞澘浣跨敤鐨勪覆鍙ｃ€�

閫氬父锛屼覆鍙ｅ湪涓嶅悓鎿嶄綔绯荤粺涓嬫樉绀虹殑鍚嶇О鏈夋墍涓嶅悓锛�

- **Windows 鎿嶄綔绯荤粺锛�** `COM1` 绛�
- **Linux 鎿嶄綔绯荤粺锛�** 浠� `/dev/tty` 寮€濮�
- **MacOS 鎿嶄綔绯荤粺锛�** 浠� `/dev/cu.` 寮€濮�

鏈夊叧濡備綍鏌ョ湅涓插彛鍚嶇О鐨勮缁嗕俊鎭紝璇疯 [涓� ESP32 鍒涘缓涓插彛杩炴帴](ref/serial_driver.md)銆�

## 閰嶇疆

璇疯繘鍏ョ浜旀锛氬紑濮嬪垱寤哄伐绋� 涓彁鍒扮殑 `hello_world` 鐩綍锛屽苟杩愯宸ョ▼閰嶇疆宸ュ叿 `menuconfig`銆�

### Linux 鍜� MacOS 鎿嶄綔绯荤粺

```
cd ~/esp/hello_world
make menuconfig
```

### Windows 鎿嶄綔绯荤粺

```
cd %userprofile%\esp\hello_world
make menuconfig
```

濡傛灉涔嬪墠鐨勬楠ら兘姝ｇ‘锛屽垯浼氭樉绀轰笅闈㈢殑鑿滃崟锛�

![](img/project-configuration.png)

杩涘叆鑿滃崟鍚庯紝閫夋嫨 `Serial flasher config` > `Default serial port` 閰嶇疆涓插彛锛堣澶囧皢閫氳繃璇ヤ覆鍙ｅ姞杞藉伐绋嬶級銆傛寜鍥炶溅閿‘璁ら€夋嫨锛岀偣鍑� `< Save >` 淇濆瓨閰嶇疆锛岀劧鍚庣偣鍑� `< Exit >` 閫€鍑� `menuconfig`銆�

`menuconfig` 宸ュ叿鐨勫父瑙佹搷浣滆涓嬨€�

- `涓婁笅绠ご`锛氱Щ鍔�
- `鍥炶溅`锛氳繘鍏ュ瓙鑿滃崟
- `ESC 閿甡锛氳繑鍥炰笂绾ц彍鍗曟垨閫€鍑�
- `鑻辨枃闂彿`锛氳皟鍑哄府鍔╄彍鍗曪紙閫€鍑哄府鍔╄彍鍗曪紝璇锋寜鍥炶溅閿級銆�
- `绌烘牸`銆乣Y 閿甡`鎴朻`N 閿甡锛氫娇鑳�/绂佺敤 `[*]` 閰嶇疆閫夐」
- `鑻辨枃闂彿` 锛氳皟鍑烘湁鍏抽珮浜€夐」鐨勫府鍔╄彍鍗�
- `/ 閿甡锛氬鎵鹃厤缃」鐩�

## 缂栬瘧鍜岀儳褰�

璇蜂娇鐢ㄤ互涓嬪懡浠わ紝缂栬瘧鐑у綍宸ョ▼锛�

```shell
make flash
```

杩愯浠ヤ笂鍛戒护鍙互缂栬瘧搴旂敤绋嬪簭鍜屾墍鏈� ESP-IDF 缁勪欢锛屾帴鐫€鐢熸垚 bootloader銆佸垎鍖鸿〃鍜屽簲鐢ㄧ▼搴忎簩杩涘埗鏂囦欢銆傛帴鐫€锛岃繖浜涗簩杩涘埗鏂囦欢灏嗚鐑у綍鑷� ESP32 寮€鍙戞澘銆�

濡傛灉涓€鍒囬『鍒╋紝鍙湪鐑у綍瀹屾垚鍚庣湅鍒扮被浼间笅鏂圭殑鎵撳嵃淇℃伅锛堜唬琛ㄥ姞杞借繘绋嬶級銆傛帴鐫€锛屽紑鍙戞澘灏嗕細澶嶄綅锛屽簲鐢ㄧ▼搴� 鈥渉ello_world鈥� 寮€濮嬪惎鍔ㄣ€�

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

濡傛灉浣跨敤 Eclipse IDE锛岃€岄潪 `make` 缂栬瘧绯荤粺锛岃鍙傝€冨畼鏂� [Eclipse 鎸囧崡](https://docs.espressif.com/projects/esp-idf/zh_CN/latest/get-started/eclipse-setup.html)銆�

## 鐩戣鍣�

浣跨敤 `make monitor` 鍛戒护锛岀洃瑙� 鈥渉ello_world鈥� 鐨勮繍琛屾儏鍐点€�

杩愯璇ュ懡浠ゅ悗锛孖DF 鐩戣鍣ㄧ敤绋嬪簭灏嗗惎鍔細

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

姝ゆ椂锛屽氨鍙互鍦ㄥ惎鍔ㄦ棩蹇楀拰璇婃柇鏃ュ織涔嬪悗锛岀湅鍒版墦鍗扮殑 鈥淗ello world!鈥� 浜嗐€�

```shell
...
Hello world!
Restarting in 10 seconds...
I (211) cpu_start:Starting scheduler on APP CPU.
Restarting in 9 seconds...
Restarting in 8 seconds...
Restarting in 7 seconds...
```

**浣跨敤蹇嵎閿� `Ctrl+]`锛岄€€鍑� IDF 鐩戣鍣ㄣ€�**

濡傛灉 IDF 鐩戣鍣ㄥ湪鐑у綍鍚庡緢蹇彂鐢熼敊璇紝鎴栨墦鍗颁俊鎭叏鏄贡鐮侊紙瑙佷笅锛夛紝寰堟湁鍙兘鏄洜涓轰綘鐨勫紑鍙戞澘閫夌敤浜� 26 MHz 鏅舵尟锛岃€� ESP-IDF 榛樿鏀寔澶у鏁板紑鍙戞澘浣跨敤鐨� 40 MHz 鏅舵尟銆�

```
e锟斤拷锟�)(Xn@锟統.!锟斤拷(锟絇W+)锟斤拷Hn9a貐/9锟�!锟絫5锟斤拷P锟絶锟絢锟斤拷e锟絜a锟�5锟絡A
~zY锟斤拷Y(1锟�,1锟斤拷 e锟斤拷锟�)(Xn@锟統.!Dr锟絲Y(锟�jpi锟絴锟�+z5Ymvp
```

姝ゆ椂锛屾寜鐓у涓嬫楠ゆ搷浣滐細

1. 閫€鍑虹洃瑙嗗櫒銆�
2. 鎵撳紑 [menuconfig](https://docs.espressif.com/projects/esp-idf/zh_CN/latest/get-started/index.html#get-started-configure)锛�
3. 杩涘叆 `Component config` 鈥�> `ESP32-specific` 鈥�> `Main XTAL frequency` 杩涜閰嶇疆锛屽皢 [CONFIG_ESP32_XTAL_FREQ_SEL](https://docs.espressif.com/projects/esp-idf/zh_CN/latest/api-reference/kconfig.html#config-esp32-xtal-freq-sel) 璁剧疆涓� 26 MHz銆�
4. 鐒跺悗锛岃閲嶆柊 [缂栬瘧鍜岀儳褰昡(https://docs.espressif.com/projects/esp-idf/zh_CN/latest/get-started/index.html#get-started-build-and-flash) 搴旂敤绋嬪簭銆�

娉ㄨВ

涔熷彲浠ヨ繍琛屼互涓嬪懡浠わ紝涓€娆℃€ф墽琛屾瀯寤恒€佺儳褰曞拰鐩戣杩囩▼锛�

```
make flash monitor
```

姝ゅ锛岃鍓嶅線 [IDF 鐩戣鍣╙(https://docs.espressif.com/projects/esp-idf/zh_CN/latest/api-guides/tools/idf-monitor.html)锛屼簡瑙ｆ洿澶氫娇鐢� IDF 鐩戣鍣ㄧ殑蹇嵎閿拰鍏朵粬璇︽儏銆�

## 鐜鍙橀噺

鐢ㄦ埛鍙互鍦ㄤ娇鐢� `make` 鍛戒护鏃� **鐩存帴璁剧疆** 閮ㄥ垎鐜鍙橀噺锛岃€屾棤闇€杩涘叆 `make menuconfig` 杩涜閲嶆柊閰嶇疆銆傝繖浜涘彉閲忓寘鎷細

| 鍙橀噺                                                         | 鎻忚堪涓庝娇鐢ㄦ柟寮�                             |
| ------------------------------------------------------------ | ------------------------------------------ |
| `ESPPORT`                                                    | 瑕嗙洊 `flash` 鍜� `monitor` 鍛戒护浣跨敤鐨勪覆鍙ｃ€� |
| 渚嬶細`make flash ESPPORT=/dev/ttyUSB1`, `make monitor ESPPORT=COM1` |                                            |
| `ESPBAUD`                                                    | 瑕嗙洊鐑у綍 ESP32 鏃朵娇鐢ㄧ殑涓插彛閫熺巼銆�          |
| 渚嬶細`make flash ESPBAUD=9600`                                |                                            |
| `MONITORBAUD`                                                | 瑕嗙洊鐩戞帶鏃朵娇鐢ㄧ殑涓插彛閫熺巼銆�                 |
| 渚嬶細`make monitor MONITORBAUD=9600`                          |                                            |

娉ㄨВ

鎮ㄥ彲瀵煎嚭鐜鍙橀噺锛堜緥锛歚export ESPPORT=/dev/ttyUSB1`锛夈€� 鍦ㄥ悓涓€浼氳瘽绐楀彛涓紝濡傛灉鏈鍚屾瑕嗙洊锛屾墍鏈� `make` 鍛戒护鍧囦細浣跨敤瀵煎嚭鐨勭幆澧冨彉閲忓€笺€�

## 鏇存柊 ESP-IDF

涔愰懌浼氫笉鏃舵帹鍑烘洿鏂扮増鏈殑 ESP-IDF锛屼慨澶� bug 鎴栨彁鍑烘柊鐨勭壒鎬с€傚洜姝わ紝鍦ㄤ娇鐢ㄦ椂锛屽簲娉ㄦ剰鏇存柊鏈湴鐨勭増鏈€傛渶绠€鍗曠殑鏂规硶鏄細鐩存帴鍒犻櫎鎮ㄦ湰鍦扮殑 `esp-idf` 鏂囦欢澶癸紝鐒跺悗鎸夌収 [绗簩姝ワ細鑾峰彇 ESP-IDF](https://docs.espressif.com/projects/esp-idf/zh_CN/latest/get-started/index.html#get-started-get-esp-idf) 涓殑鎸囩ず锛岄噸鏂板畬鎴愬厠闅嗐€�

濡傛灉甯屾湜灏� ESP-IDF 鍏嬮殕鍒版柊鐨勮矾寰勪笅锛岃鍔″繀 [閲嶆柊璁剧疆 IDF_PATH](https://docs.espressif.com/projects/esp-idf/zh_CN/latest/get-started/add-idf_path-to-profile.html)銆傚惁鍒欙紝宸ュ叿閾惧皢鏃犳硶鎵惧埌 ESP-IDF銆�

姝ゅ锛屾偍鍙互浠呮洿鏂板彉鏇撮儴鍒嗐€傚叿浣撴柟寮忥紝璇峰墠寰€ [鏇存柊](https://docs.espressif.com/projects/esp-idf/zh_CN/latest/versions.html#updating) 绔犺妭鏌ョ湅銆�