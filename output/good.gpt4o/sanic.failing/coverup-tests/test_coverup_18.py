# file sanic/exceptions.py:9-21
# lines [9, 14, 15, 16, 17, 18, 19, 21]
# branches ['16->17', '16->18']

import pytest
from sanic.exceptions import SanicException

_sanic_exceptions = {}

def add_status_code(code, quiet=None):
    """
    Decorator used for adding exceptions to :class:`SanicException`.
    """

    def class_decorator(cls):
        cls.status_code = code
        if quiet or quiet is None and code != 500:
            cls.quiet = True
        _sanic_exceptions[code] = cls
        return cls

    return class_decorator

def test_add_status_code():
    @add_status_code(404)
    class NotFound(SanicException):
        pass

    @add_status_code(500, quiet=False)
    class ServerError(SanicException):
        pass

    @add_status_code(400, quiet=True)
    class BadRequest(SanicException):
        pass

    assert NotFound.status_code == 404
    assert NotFound.quiet is True
    assert _sanic_exceptions[404] is NotFound

    assert ServerError.status_code == 500
    assert not hasattr(ServerError, 'quiet')
    assert _sanic_exceptions[500] is ServerError

    assert BadRequest.status_code == 400
    assert BadRequest.quiet is True
    assert _sanic_exceptions[400] is BadRequest

    # Clean up
    _sanic_exceptions.clear()
