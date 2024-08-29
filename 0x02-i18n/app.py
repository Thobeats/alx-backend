#!/usr/bin/env python3
"""
A Basic flask application
"""
from typing import (
    Dict, Union
)

from flask import Flask
from flask import g, request
from flask import render_template
from flask_babel import Babel, format_datetime
import pytz
import datetime


class Config(object):
    """
    Application configuration class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Instantiate the application object
app = Flask(__name__)
app.config.from_object(Config)

# Wrap the application with Babel
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale() -> str:
    """
    Gets locale from request object
    """
    if 'locale' in request.args:
        locale = request.args.get('locale', 0)
        return locale
    else:
        locale = get_user(request.args.get('login_as', 0))
        if locale and locale['locale'] in Config.LANGUAGES:
            return locale['locale']
        else:
            return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """
    Gets timezone from request object
    """
    current_timezone = app.config['BABEL_DEFAULT_TIMEZONE']
    if 'timezone' in request.args:
        timezone = request.args.get('timezone', 0)
        current_timezone = timezone
    else:
        timezone = get_user(request.args.get('login_as', 0))
        if timezone and timezone['timezone'] in Config.LANGUAGES:
            current_timezone = timezone['timezone']

    try:
        return pytz.timezone(current_timezone).zone
    except pytz.exceptions.UnknownTimeZoneError as e:
        return app.config['BABEL_DEFAULT_TIMEZONE']


def get_user(id) -> Union[Dict[str, Union[str, None]], None]:
    """
    Validate user login details
    Args:
        id (str): user id
    Returns:
        (Dict): user dictionary if id is valid else None
    """
    return users.get(int(id), 0)


@app.before_request
def before_request():
    """
    Adds valid user to the global session object `g`
    Adds the current_time_zone the global session g
    """
    setattr(g, 'user', get_user(request.args.get('login_as', 0)))
    setattr(g, 'current_time', format_datetime(datetime.datetime.now()))



@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders a basic html template
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5001, debug=True)
