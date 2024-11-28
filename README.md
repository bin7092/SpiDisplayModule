**功能描述**：在Orange Pi5主板上，通过Python语言实现对1.69寸IPS彩色LCD（SPI接口）屏幕的点亮操作。

**所涉主板及屏幕**：
- **主板**：Orange Pi5。
- **屏幕**：1.69寸IPS彩色LCD，采用SPI接口。

**使用的库及安装说明**：
- 用到的库如下：
    - `import wiringpi`：关于其安装方式，请查阅Orangpi的相关文档。
    - `import spidev`。
    - `from smbus import SMBus`。
    - `import numpy as np`。

**项目代码部分介绍**：
- **lcdconfig.py**：这是一个与硬件进行通信的类，在整个点亮屏幕的操作中起着关键作用，负责建立代码与硬件之间的联系，实现数据的传输等功能。
- **ImageUtil.py**：属于image的工具类，其中包含两个重要方法：
    - `rotate_image(image, rotation_angle)`：该方法可将传入的image按照指定的旋转角度进行旋转方向的操作。在实际使用过程中，若屏幕接受数组后的数据填充方式与预期不符（比如自己的屏幕是将数据竖向填充，而示例中的屏幕是横向填充），就需要调用此方法先对图片进行旋转方向的调整。
    - `convert_image_to_pix(image)`：此方法用于将传入的image转换为数组形式，以便后续能够符合屏幕显示所需的数据格式要求，顺利在屏幕上进行显示。

**注意事项**：
由于屏幕的生产厂商可能不同，在使用过程中可能会出现数据填充方式的差异。即可能存在这样的情况：自己的屏幕在接收到数组后，是将数据依次横向填充在屏幕上面，但示例中的屏幕却是竖向填充在屏幕上。此时，就需要调用ImageUtil.py中的`rotate_image`方法先将图片旋转方向，然后再调用`convert_image_to_pix`方法，将iamge转为数组，以确保屏幕能够正确显示图像。

**扩展内容**：
当前给出的是针对1.69英寸屏幕的示例，但在项目中，已经对底层代码进行了合理拆分。所以，如果使用的是其他尺寸的屏幕，无需对`lcdconfig.py`和`ImageUtil.py`这两个文件进行修改，只需模仿`LCD_1inch69.py`文件的编写方式，创建一个适合自己屏幕尺寸的驱动即可。