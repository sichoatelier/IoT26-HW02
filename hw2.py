from gpiozero import LED, Button
from signal import pause

led = LED(14)
button = Button(4)

print("Program started. LED (GPIO 14) is controlled by input on GPIO 4.")
print("Current input value (0 or 1):", button.value)

button.when_pressed = led.on
button.when_released = led.off

try:
    pause()
except KeyboardInterrupt:
    print("\nProgram terminated.")
