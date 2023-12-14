import os
import flask
import dotenv

from src import camera, settings, utils


def create_app():
    # Load environment variables
    dotenv.load_dotenv()

    # Create App and Load Config
    app = flask.Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY"),
    )

    # Define the Routes
    build_routes(app)

    return app


def build_routes(app):
    @app.route("/")
    def index():
        return flask.render_template_string("""
        <form action="/exec_capture" method="POST">
            <input type="submit" value="Capture">
        </form>
        <form action="/exec_start_timelapse" method="POST">
            <input type="submit" value="Start Timelapse">
        </form>
        
        <!--- Print Messages -->
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <script>alert('{{ category }}: {{ message }}')</script>
                {% endfor %}
            {% endif %}
        {% endwith %}
        """)

    # Server Routes
    @app.route("/exec_capture", methods=["POST"])
    def exec_capture():
        camera.take_photo()
        flask.flash("Capturing Photo")
        return flask.redirect(flask.url_for("index"))

    @app.route("/exec_start_timelapse", methods=["POST"])
    def exec_start_timelapse():
        camera.start_timelapse()
        flask.flash("Timelapse has started")
        return flask.redirect(flask.url_for("index"))
