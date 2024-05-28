#!/usr/bin/env python3
"""
Basic Babel
"""

from flask_babel import Babel

babel = Babel()


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"  # Set default language to English
    BABEL_DEFAULT_TIMEZONE = "UTC"
