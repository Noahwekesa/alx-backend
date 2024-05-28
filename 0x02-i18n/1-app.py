from flask import Flask
from flask_babel import Babel

app = Flask(__name__)
app.config.from_pyfile("mysettings.cfg")
babel = Babel(app)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"  # Set default language to English
    BABEL_DEFAULT_TIMEZONE = "UTC"
