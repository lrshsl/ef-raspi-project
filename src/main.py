
from flask import Flask, url_for, render_template, request, jsonify, redirect
import os

IMAGE_FOLDER = os.path.join('static', 'images')



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER



# TODO: make OOP


@app.route("/")
@app.route('/index')
def index():
    return render_template("index.html")


@app.route("/live_photos")
def live_photos():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'photo.png')
    app.config['live_photo_path'] = full_filename
    return render_template("live_photos.html")



# File picker, from this stackoverflow answer: https://stackoverflow.com/questions/23775211/flask-desktop-application-file-chooser
import tkinter as tk
from tkinter.filedialog import askopenfilename

@app.route('/filedialog', methods = ['POST'])
def filedialog():
    """open file dialog to get a file name"""

    filename = 'not found'
    root = tk.Tk()
    root.withdraw()

    try:
        filename = askopenfilename()
    except tk.TclError:
        return redirect(url_for('live_photos'))

    if filename == 'not found':
        root.mainloop()
    else:
        root.destroy()
        app.config['live_photo_path'] = filename

    return redirect(url_for('live_photos'))

