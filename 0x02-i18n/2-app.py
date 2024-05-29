#!/usr/bin/env python3
"""Get locale from request"""

from flask import Flask, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get locale from request"""
    return request.accept_languages.best_match(["en", "fr"])
