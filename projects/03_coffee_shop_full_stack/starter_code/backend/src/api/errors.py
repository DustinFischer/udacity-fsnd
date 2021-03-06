from flask import jsonify

from . import api
from .auth import AuthError


def error_json(err):
    return jsonify({
        'error': f'{err.code}: {err.name}',
        'message': err.description
    }), err.code


@api.app_errorhandler(400)
def bad_request(err):
    return error_json(err)


@api.app_errorhandler(404)
def not_found(err):
    return error_json(err)


@api.app_errorhandler(405)
def method_not_allowed(err):
    return error_json(err)


@api.app_errorhandler(422)
def unprocessable_entity(err):
    return error_json(err)


@api.app_errorhandler(500)
def server_error(err):
    return error_json(err)


@api.errorhandler(AuthError)
def handle_auth_error(exc):
    # TODO: Conform with above
    response = jsonify(exc.error)
    response.status_code = exc.status_code
    return response
