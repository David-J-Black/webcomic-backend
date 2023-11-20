from functools import wraps
import flask
from flask import jsonify, request
import bcrypt
from logger import log

import config

bad_security_response: dict[str, any] = {
    'message': 'https://youtu.be/RfiQYRn7fBg?si=Ux7auqJ7lYpFxbeY&t=10'
}

def _is_public_authenticated():
    # Grab the headers from the incoming request

    headers = flask.request.headers
    log.info(f'Checking the authentication for...[{headers}]')

    security_question: str | None = headers.get('doYouThinkImPretty')
    log.info(f'Response to security question...[{security_question}]')

    if security_question == 'yes':
        print('Request passed authentication')
    else:
        print(f'Request failed auth! {request.host_url}')
        return jsonify(bad_security_response), 403


def _is_admin_authenticated():
    # Get headers
    headers = flask.request.headers
    auth: str = headers['Authorization']

    if auth is None:
        return jsonify(bad_security_response), 403

    # encode included token and see if we have a match...
    password_bytes = auth.encode('utf-8')
    stored_pass = config.admin_pass_hashed.encode('utf-8')
    match: bool = bcrypt.checkpw(password_bytes, stored_pass)

    if not match:
        return jsonify(bad_security_response), 403


def secure_route(route_function):
    @wraps(route_function)
    def wrapper(*args, **kwargs):
        result = _is_public_authenticated()
        log.info('Incoming request')
        if result is not None:
            return jsonify(bad_security_response), 403
        return route_function(*args, **kwargs)

    return wrapper


def admin_secure(route_function):
    @wraps(route_function)
    def wrapper(*args, **kwargs):
        log.info(f'Incoming request:{flask.request.__dict__}')
        result = _is_admin_authenticated()

        if result is not None:
            return result
        return route_function(*args, **kwargs)

    return wrapper
