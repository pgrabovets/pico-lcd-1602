from machine import Pin
from utime import sleep_ms, sleep_us


LCD_4BIT_MOD = 0b00000010
LCD_4BIT_2LINES = 0b00101000
LCD_DISPLAY_ON = 0b00001100
LCD_CLEAR = 0b00000001
LCD_HOME = 0b00000010
LCD_SHIFT_R = 0b00010100
LCD_SHIFT_L = 0b00010000


class LCD1602:
    def __init__(self, **config):
        self.enable = Pin(config['e'], Pin.OUT)
        self.rs = Pin(config['rs'], Pin.OUT)
        self.d4 = Pin(config['d4'], Pin.OUT)
        self.d5 = Pin(config['d5'], Pin.OUT)
        self.d6 = Pin(config['d6'], Pin.OUT)
        self.d7 = Pin(config['d7'], Pin.OUT)
        
        self.rs.value(0)
        self.set_4bit_data(LCD_4BIT_MOD)
        self.set_8bit_data(LCD_4BIT_2LINES)
        self.set_8bit_data(LCD_DISPLAY_ON)
        self.set_8bit_data(LCD_CLEAR)
        sleep_ms(16)
        self.set_8bit_data(LCD_HOME)
        sleep_ms(16)

    def pulse_enable(self):
        self.enable.value(0)
        sleep_us(2)
        self.enable.value(1)
        sleep_us(2)
        self.enable.value(0)
        sleep_us(100)

    def set_4bit_data(self, data):
        lo_nibble = data & 0x0F
        self.d7.value(lo_nibble & 0x08)
        self.d6.value(lo_nibble & 0x04)
        self.d5.value(lo_nibble & 0x02)
        self.d4.value(lo_nibble & 0x01)
        self.pulse_enable()

    def set_8bit_data(self, data):
        hi_nibble = data >> 4
        lo_nibble = data & 0x0F
        self.d7.value(hi_nibble & 0x08)
        self.d6.value(hi_nibble & 0x04)
        self.d5.value(hi_nibble & 0x02)
        self.d4.value(hi_nibble & 0x01)
        self.pulse_enable()
        self.d7.value(lo_nibble & 0x08)
        self.d6.value(lo_nibble & 0x04)
        self.d5.value(lo_nibble & 0x02)
        self.d4.value(lo_nibble & 0x01)
        self.pulse_enable()

    def print_char(self, char):
        self.rs.value(1)
        self.set_8bit_data(ord(char))

    def print_str(self, string):
        self.rs.value(1)
        for s in string:
            self.print_char(s)

    def clear(self):
        self.rs.value(0)
        self.set_8bit_data(LCD_CLEAR)
        sleep_ms(6)

    def cursor_home(self):
        self.rs.value(0)
        self.set_8bit_data(LCD_HOME)
        sleep_ms(16)

    def cursor_shift(self, value):
        self.rs.value(0);
        for position in range(value):
            self.set_8bit_data(LCD_SHIFT_R)
