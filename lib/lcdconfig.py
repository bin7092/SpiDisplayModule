import logging
import os
import sys
import time
import spidev
import wiringpi


class OrangePi:
    def __init__(self, spi=spidev.SpiDev(4, 1), spi_freq=40000000, rst=10, dc=16, bl=13):
        wiringpi.wiringPiSetup()

        self.INPUT = 0
        self.OUTPUT = 1

        self.SPEED = spi_freq

        self.RST_PIN = rst
        self.gpio_mode(self.RST_PIN, self.OUTPUT)
        self.DC_PIN = dc
        self.gpio_mode(self.DC_PIN, self.OUTPUT)
        self.BL_PIN = bl
        self.gpio_mode(self.BL_PIN, self.OUTPUT)
        self.digital_write(self.BL_PIN, 1)

        #Initialize SPI
        self.SPI = spi
        if self.SPI != None:
            self.SPI.max_speed_hz = spi_freq
            self.SPI.mode = 0b00

    def gpio_mode(self, Pin, Mode):
        if Mode:
            return wiringpi.pinMode(Pin, self.OUTPUT)
        else:
            return wiringpi.pinMode(Pin, self.INPUT)

    def digital_write(self, Pin, value):
        if value:
            wiringpi.digitalWrite(Pin, 1)
        else:
            wiringpi.digitalWrite(Pin, 0)

    def digital_read(self, Pin):
        return wiringpi.digitalRead(Pin)

    def delay_ms(self, delaytime):
        wiringpi.delay(delaytime)

    def gpio_pwm(self, Pin):
        wiringpi.pinMode(Pin, self.OUTPUT)
        wiringpi.softPwmCreate(Pin, 0, 100)

    def spi_writebyte(self, data):
        if self.SPI != None:
            self.SPI.writebytes(data)

    def module_init(self):
        if self.SPI != None:
            self.SPI.max_speed_hz = self.SPEED
            self.SPI.mode = 0b00
        return 0

    def module_exit(self):
        logging.debug("spi end")
        if self.SPI != None:
            self.SPI.close()

        logging.debug("gpio cleanup...")
        self.digital_write(self.RST_PIN, 1)
        self.digital_write(self.DC_PIN, 0)
        self.digital_write(self.BL_PIN, 0)
        time.sleep(0.001)


