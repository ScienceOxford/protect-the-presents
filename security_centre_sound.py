from microbit import *
import speech
import radio

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

radio.on()

while True:
    incoming = radio.receive()
    if incoming is not None:
        speech.say(incoming)
    sleep(500)
