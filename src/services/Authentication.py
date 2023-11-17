from functools import wraps
from app import webcomic_config, log
import flask
from flask import jsonify, request
import bcrypt



def is_public_authenticated():
    # Grab the headers from the incoming request
    headers = flask.request.headers
    security_question: str | None = headers['doYouThinkImPretty']
    if security_question == 'yes':
        print('Request passed authentication')
    else:
        print(f'Request failed auth! {request.host_url}')
        return jsonify({'message': "Ah ah ah, you didn\'t say the magic word!"}), 403


def is_admin_authenticated():
    # Get headers
    headers = flask.request.headers
    auth: str = headers['Authorization']

    if auth is None:
        return jsonify({'message': "Ah ah ah, you didn\'t say the magic word!"}), 403

    # encode included token and see if we have a match...
    password_bytes = auth.encode('utf-8')
    stored_pass = webcomic_config.admin_pass_hashed.encode('utf-8')
    match: bool = bcrypt.checkpw(password_bytes, stored_pass)

    if not match:
        return jsonify({'message': "Ah ah ah, you didn\'t say the magic word!"}), 403

def secure_route(route_function):
    @wraps(route_function)
    def wrapper(*args, **kwargs):
        result = is_public_authenticated()
        log.info('Incoming request')
        if result is not None:
            return result
        return jsonify({'message': "Ah ah ah, you didn\'t say the magic word!"}), 403

    return wrapper


def admin_secure(route_function):
    @wraps(route_function)
    def wrapper(*args, **kwargs):
        log.info(f'Incoming request:{flask.request.__dict__}')
        result = is_admin_authenticated()

        if result is not None:
            return result
        return route_function(*args, **kwargs)

    return wrapper
