from microbit import *
import neopixel
import radio

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

np = neopixel.NeoPixel(pin2, 18)

radio.on()

while True:
    incoming = radio.receive()
    while incoming is None:
        incoming = radio.receive()
        for pixel_id in range(0, len(np)):
            np[pixel_id] = (0, 60, 0)
        np.show()
        display.show(Image.XMAS)
        sleep(100)
    display.show(Image.ANGRY)
    for i in range(0, 10):
        for pixel_id in range(0, len(np)):
            np[pixel_id] = (60, 0, 0)
        np.show()
        sleep(100)
        np.clear()
        sleep(100)
