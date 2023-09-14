# pico-lcd-1602 4-bit mode

This is a simple lib for a Raspberry Pi PICO and control it with micropython.
Supports only 4-bit mode

```python
from lcd1602 import LCD1602

lcd = LCD1602(e=16, rs=17, d4=21, d5=20, d6=19, d7=18)

lcd.clear()
lcd.cursor_home()
lcd.print_str('Hello world!')
lcd.cursor_home()
lcd.cursor_shift(40)
lcd.print_char('H')
```
