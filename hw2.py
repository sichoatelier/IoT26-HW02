from gpiozero import DigitalInputDevice, LED
from signal import pause

led = LED(14)
input = DigitalInputDevice (4)

print(input.value)

input.when_activated = led.on
input.when_deactivated =led.off

pause()