from machine import Pin, I2C
import time
import ssd1306

# ---------- OLED ----------
i2c = I2C(0, scl=Pin(7), sda=Pin(6))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

# ---------- ENCODER ----------
enc_a = Pin(28, Pin.IN, Pin.PULL_UP)
enc_b = Pin(29, Pin.IN, Pin.PULL_UP)
last_a = enc_a.value()

# ---------- BUTTONS ----------
sw1 = Pin(3, Pin.IN, Pin.PULL_UP)
sw2 = Pin(4, Pin.IN, Pin.PULL_UP)

# ---------- STATE ----------
mode = 0   # 0 = play, 1 = time set (mode 2)
minutes = 0  # 00:00
last_min_tick = time.ticks_ms()
last_toggle = 0

# ---------- HELPERS ----------
def draw_time():
    h = minutes // 60
    m = minutes % 60
    oled.fill(0)
    oled.text(f"{h:02d}:{m:02d}", 32, 12)
    oled.show()

draw_time()

# ---------- MAIN ----------
while True:
    now = time.ticks_ms()

    # ----- minute ticker -----
    if time.ticks_diff(now, last_min_tick) >= 60000:
        minutes = (minutes + 1) % 1440
        last_min_tick = now
        draw_time()

    # ----- mode toggle (SW1 + SW2) -----
    if not sw1.value() and not sw2.value():
        if time.ticks_diff(now, last_toggle) > 500:
            mode = 1 - mode
            last_toggle = now
        time.sleep_ms(200)

    # ----- encoder -----
    a = enc_a.value()
    if a != last_a:
        step = 1 if enc_b.value() != a else -1

        if mode == 1:  # TIME ADJUST MODE
            minutes = (minutes + step) % 1440
            draw_time()

        last_a = a
        time.sleep_ms(3)
