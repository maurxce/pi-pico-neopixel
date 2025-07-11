from machine import Pin
from utime import sleep_ms
from neopixel import NeoPixel

# Color Configuration
LED_ON = (255, 255, 255)
LED_OFF = (0, 0, 0)

# Hardware Configuration
LED_COUNT = 34
LED_PIN = 18
BUTTON_PIN = 19
DEBUG_LED_PIN = 25

# Delay Configuration
LED_UPDATE_DELAY_MS = 25
BUTTON_DEBOUNCE_DELAY_MS = 50

# Initialize Hardware
# LED_R - 5V (VBUS)
# LED_G - Data
# LED_W - GND
led_strip = NeoPixel(Pin(LED_PIN), LED_COUNT)
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)
debug_led = Pin(DEBUG_LED_PIN, Pin.OUT)

# State variables
toggled = False
previous = True # Assume button is not pressed initially

def set_led_color(color: tuple[int, int, int], delay: int = LED_UPDATE_DELAY_MS) -> None:
    """
    Set the color of all LEDs on the strip with a delay between each update.
    
    Args:
        color (tuple[int, int, int]): The color to set the LEDs to.
        delay (int): The delay in milliseconds between updating each LED.
    """
    for i in range(LED_COUNT):
        led_strip[i] = color
        led_strip.write()
        sleep_ms(delay)

def toggle_leds(state: bool) -> None:
    """
    Toggle the LEDs on or off based on the given state.

    Args:
        state (bool): If True, turn LEDs on; otherwise, turn them off.
    """
    debug_led.value(state)
    color = LED_ON if state else LED_OFF
    set_led_color(color)

while True:
    current = button.value()
    
    if previous and not current:
        toggled = not toggled
        print(f"Toggled: {toggled}")
        toggle_leds(toggled)
    
    previous = current
    sleep_ms(BUTTON_DEBOUNCE_DELAY_MS)
