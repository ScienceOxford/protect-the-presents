from microbit import *
import neopixel
import radio

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

np = neopixel.NeoPixel(pin0, 18)
red = (60, 0, 0)
green = (0, 60, 0)
blue = (0, 0, 60)

radio.on()

while True:
    display.show(Image.ANGRY)
    # messages will be received on channels 10-27
    for x in range (10, len(np)+10):
        radio.config(channel=x)
        message = radio.receive()
        if message == 'thief':
            np[x-10] = red
        elif message == 'safe':
            np[x-10] = green
        else:
            np[x-10] = blue
        np.show()
    sleep(1)
