from microbit import *
import radio

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

names = {'donner': 13, 'dasher': 14, 'comet': 15,
         'dancer': 16, 'vixen': 17, 'blitzen': 18}

name = names.get('blitzen')

radio.on()
radio.config(channel=name)

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(Image.ARROW_N)
        radio.send('forward')
    elif button_a.is_pressed():
        radio.send('left')
        display.show(Image.ARROW_W)
    elif button_b.is_pressed():
        radio.send('right')
        display.show(Image.ARROW_E)
    else:
        radio.send('stop')
        display.clear()
    sleep(1)
