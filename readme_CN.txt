这个文件是帮助您使用本例程。

1.基本信息：
本例程使用单独LCD模块进行了验证，你可以在工程的Examples\中查看对应的测试例程;
本例程均在Orange Pi 5上进行了验证;

2.管脚连接：
管脚连接你可以在 \lib\lcdconfig.py中查看，这里也再重述一次：
EPD  	=>	OrangePI(rk3588)
VCC    	->    	3.3V
GND    	->    	GND
DIN    	->    	11(SPI4_MOSI)
CLK    	->    	14(SPI4_SCK)
CS     	->    	15(SPI4_CS1)
DC     	->    	16
RST    	->    	10
BL  	->    	13

3.安装库：
    # 根据Orange PI的文档，安装wiringOP-Python
    sudo apt-get update
    sudo apt-get install python3-pip
    sudo apt-get install python3-pil
    sudo apt-get install python3-numpy
    sudo apt-get update
    # i2c
    sudo apt-get install python3-smbus

4.基本使用：
由于本工程是一个综合工程，对于使用而言，你可能需要阅读以下内容：
你可以在examples\目录中查看测试程序
请注意你购买的是哪一款的LCD模块。
栗子：
    如果你购买的1.54inch LCD，那么你应该执行命令：
    sudo python ./1inch54_LCD_test.py

 
