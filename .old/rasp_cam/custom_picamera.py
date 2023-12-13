from typing import Optional, Union
import time
import picamera


class PiCamera(picamera.PiCamera):

    def __init__(self,
                 record_name: str,
                 images_folder: str,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.record_name = record_name
        self.photos_folder = images_folder
        self.photos_id = 0

    def take_photo(self):
        self.capture('{path}/_{record}_photo{photo_id}.png'.format(
            path = self.photos_folder,
            record = self.record_name,
            photo_id = self.photos_id))
        self.photos_id += 1

    async def take_photos_async(self,
                                period_length: Union[int, float] = 5,         # Default: all 5 seconds a photo
                                duration: Union[int, float] = float('inf'),   # Until interrupted. Not used, if nphotos is provided
                                nphotos: Optional[int]=None):           # Maximum number of photos to be taken
        if nphotos is not None:
            duration = nphotos * period_length

        start_time = time.time()
        while time.time() - start_time <= duration:
            self.take_photo()
            time.sleep(period_length)

