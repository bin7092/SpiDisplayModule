import time
from PIL import Image
from lib import ImageUtil


def ShowImage(image):
    """Set buffer to value of Python Imaging Library image."""
    """Write display buffer to physical display"""
    image = ImageUtil.scale_and_crop_image(image, 240, 280)
    image = ImageUtil.rotate_image(image, 90)
    print(image.width, image.height)
    pix = ImageUtil.convert_image_to_pix(image)
    print(len(pix))
    for i in range(0, len(pix), 4096):
        print(i, i + 4096)
        # self.spi_writebyte(pix[i:i + 4096])


if __name__ == '__main__':
    # ImagePath = ["../pic/LCD_1inch69_4.jpg", "../pic/LCD_1inch69_5.jpg", "../pic/LCD_1inch69_6.jpg"]
    ImagePath = ["../pic/LCD_1inch69_4.jpg"]
    for i in range(0, 1):
        image = Image.open(ImagePath[i])
        # image = image.rotate(0)
        ShowImage(image)
        time.sleep(2)