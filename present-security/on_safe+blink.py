from microbit import *
import radio

radio.on()

warn0 = Image('00000:00000:00000:00000:00000')
warn4 = Image('44444:44444:44444:44444:44444')
warn9 = Image('99999:99999:99999:99999:99999')
blink = [warn0, warn4, warn9, warn4, warn0]

while True:
    display.show(Image.XMAS)
    if pin0.is_touched():
        radio.send('present 1 safe')
        sleep(500)
    else:
        radio.send('present 1 warning')
        sleep(1)
        display.show(blink, delay=50)
