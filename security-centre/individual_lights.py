from microbit import *
import neopixel
import radio

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

np = neopixel.NeoPixel(pin2, 18)

radio.on()

presents = {'1': (0, 5, 6),
            '2': (1, 4, 7),
            '3': (2, 3, 8),
            '4': (15, 14, 9),
            '5': (16, 13, 10),
            '6': (17, 12, 11)}

for pixel_id in range(0, len(np)):
    np[pixel_id] = (0, 60, 0)
np.show()

while True:
    incoming = radio.receive()
    
    if incoming is not None:
        message = incoming.split()
        column = presents.get(message[1])
        
        if message[2] == 'safe':
            for pixel in column:
                np[pixel] = (0, 60, 0)
            display.show(Image.XMAS)

        elif message[2] == 'warning':
            for pixel in column:
                np[pixel] = (60, 0, 0)
            display.show(Image.ANGRY)

        np.show()
        sleep(100)
