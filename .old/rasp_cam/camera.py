
import constants
import picamera
import time
import grovepi

grovepi.pinMode(constants.CAMERA_PIN, "INPUT")


def take_picture():
    camera = picamera.PiCamera()
    camera.start_preview()

    camera.capture('/home/pi/output/v1_{timestamp}.jpg'.format(timestamp=time.now()))
    time.sleep(10)

    camera.stop_preview()


while True:
    try:
        if grovepi.digitalRead(button):
            take_picture()
        time.sleep(1000)
    except IOError:
        print("IOError: Recovering")


