from io import BytesIO
import os
import time
from datetime import datetime

from src import settings

# Can't install picamera module if not on Raspberry Pi
if settings.on_raspberry_pi:
    from picamera import PiCamera
    from picamera.array import PiRGBArray
else:
    from src.picamera_mock import PiCamera, PiRGBArray


# Camera
picamera = PiCamera()
stream = BytesIO()

start_time = datetime.now()


def take_photo():
    time.sleep(0.1) # Warmup

    capture_path = os.path.join(settings.images_folder,
                                 datetime.now().strftime('img%Y-%m-%d-%H-%M-%S.jpg'))

    with open(capture_path, 'w') as f:
        picamera.capture(f, 'jpeg')
    print(f'--< [Camera] Captured to {capture_path} >--')

    # image = raw_image.array
    #cv2.imshow("Image", image)


# Timelapse
def start_timelapse():
    import threading
    thread = threading.Thread(target=capture_timelapse, args=())
    thread.start()

def capture_timelapse():
    frame: int = 0
    for filename in picamera.capture_continuous(
            os.path.join(settings.timelapses_folder,
                         f'capture{settings.capture_name}_{frame}' +
                         '{timestamp:%Y-%m-%d-%H-%M}.jpg')):
        wait()
        print('Captured frame {frame}: {filename}'.format())


def wait():

    # Stop if timelapse duration is over
    now = datetime.now()
    if now < start_time:
        return False

    # Else wait for the next capture
    delay = settings.interval_minutes * 60
    time.sleep(delay)
    return True


