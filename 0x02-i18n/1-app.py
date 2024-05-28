#!/usr/bin/env python3
"""
Basic Babel
"""

from flask_babel import Babel


babel = Babel()


class Config:
    """Config class"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
