from microbit import *
import radio

radio.on()

warn0 = Image('00000:00000:00000:00000:00000')
warn4 = Image('44444:44444:44444:44444:44444')
warn9 = Image('99999:99999:99999:99999:99999')
blink = [warn0, warn4, warn9, warn4, warn0]

while True: 
    if pin0.is_touched() is False:
        radio.send('Stop thief!')
        display.show(blink, delay=50)
        sleep(1000)
    else:
        display.clear()
