import os

on_raspberry_pi: bool = False
images_folder: str = 'output/images/'
timelapses_folder: str = 'output/timelapses/'
camera_port: int = 0

interval_minutes: float = 0.3
recording_duration_minutes: float = 10


def load_settings():
    """
    Load settings from environment variables
    """
    global images_folder, camera_port, timelapses_folder, on_raspberry_pi

    # Not optional: ON_RASPBERRY_PI
    on_pi = os.getenv('ON_RASPBERRY_PI')
    assert on_pi is not None, 'ON_RASPBERRY_PI not set'
    on_raspberry_pi = bool(on_pi)

    # Optional: IMAGES_FOLDER
    path = os.getenv('IMAGES_FOLDER')
    if path is not None:
        images_folder = path
    
    # Optional: TIMELAPSES_FOLDER
    timelapses_path = os.getenv('TIMELAPSES_FOLDER')
    if timelapses_path is not None:
        timelapses_folder = timelapses_path

    # Not optional: CAMERA_PORT
    port = os.getenv('CAMERA_PORT')
    if port is not None:
        camera_port = int(port)
    else:
        # No default, needs to be set explicitly
        raise Exception('CAMERA_PORT not set')

    interval_minutes = os.getenv('INTERVAL_MINUTES')
    assert interval_minutes is not None, 'INTERVAL_MINUTES not set'

    recording_duration_minutes = os.getenv('RECORDING_DURATION_MINUTES')
    assert recording_duration_minutes is not None, 'RECORDING_DURATION_MINUTES not set'

