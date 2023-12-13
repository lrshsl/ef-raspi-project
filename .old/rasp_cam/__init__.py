
from flask import url_for, render_template, request, redirect
import flask
import os
import numpy as np

# from custom_picamera import PiCamera
from .custom_picamera import PiCamera

# Load .env file
from dotenv import load_dotenv
load_dotenv()


### ----- Constants ----- ###

DEFAULT_IMAGE_FOLDER = os.path.join('static', 'images')



### ----- Flask app initialization ----- ###

# TODO: make OOP

def create_app(*args):
    app = flask.Flask(__name__)
    app.secret_key = os.getenv('SECRET_KEY')

    app.config['default_interval_seconds'] = os.getenv('default_interval_seconds')
    app.config['default_recording_duration_minutes'] = os.getenv('default_recording_duration_minutes')

    ### ----- App routes ----- ###


    # Index
    @app.route('/')
    @app.route('/index')
    def index():
        flask.session['live_photo_path'] = DEFAULT_IMAGE_FOLDER
        return render_template('index.html')

    @app.route('/submit_start_recording', methods=['POST'])
    def submit_start_recording():
        MainState().start_recording()
        return 'Recording started'

    # Settings
    @app.route('/settings')
    def settings():
        return render_template('settings.html')

    @app.route('/settings_submit', methods=['POST'])
    def process_settings():
        return SettingsManager.update_settings()

    # Live preview
    @app.route('/video_feed')
    def video_feed():
        return Response(Stream.get_instance().generate_frames(),
                        mimetype='multipart/x-mixed-replace; boundary=frame')

    @app.route('/live_photos')
    def stream():
        return render_template('live_photos.html')

    return app


class SettingsManager:
    @staticmethod
    def update_settings():
        interval_sec = request.form.get('interval_sec')
        duration_min = request.form.get('duration_min')
        if not interval_sec or not duration_min:
            flask.flash('Error: interval_sec and duration_min must be provided.\
                    Please enter a number in the all given input fields',
                        'error')
            return redirect(url_for('settings'))

        # Now you can use these values for further processing
        # For example, you can convert them to integers for calculations
        interval_sec = int(interval_sec)
        duration_min = int(duration_min)

        # TODO

        flask.flash('Settings saved', 'success')
        return redirect(url_for('index'))


class MainState:
    instance = None

    # Implement singleton pattern
    def __new__(cls):
        if cls.instance is not None:
            return cls.instance
        cls.instance = super(MainState, cls).__new__(cls)
        return cls.instance

    def __init__(self, app):
        self.camera = PiCamera()
        self.recording = False
        self.app = app

    def start_recording(self):
        self.recording = True
        self.camera.take_photos_async(
                period_length=self.app['interval_seconds'],
                duration=self.app['recording_duration_minutes'],
                nphotos=None)


class Stream:
    instance = None

    @staticmethod
    def get_instance():
        if Stream.instance is None:
            Stream.instance = Stream('camplaceholder')
        return Stream.instance

    def __init__(self, camera):
        self.camera = camera

    def next_frame(self):
        while True:
            # Capture a frame from the camera
            frame = np.empty((self.camera.resolution[1],
                              self.camera.resolution[0], 3), dtype=np.uint8)
            camera.capture(frame, 'bgr')

            # Encode the frame as JPEG
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' +
                   frame.tobytes() + b'\r\n')





