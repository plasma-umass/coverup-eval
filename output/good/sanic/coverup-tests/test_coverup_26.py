# file sanic/exceptions.py:234-249
# lines [234, 244, 245, 247, 248, 249]
# branches ['244->245', '244->248']

import pytest
from sanic.exceptions import SanicException, abort
from sanic.helpers import STATUS_CODES

# Mocking the _sanic_exceptions dictionary to simulate different status codes
_sanic_exceptions = {
    400: SanicException,
    404: SanicException,
    500: SanicException
}

# Test function to cover abort function with a status code that has a custom message
def test_abort_with_custom_message(mocker):
    mocker.patch('sanic.exceptions._sanic_exceptions', _sanic_exceptions)
    
    with pytest.raises(SanicException) as exc_info:
        abort(400, "Custom Error Message")
    
    assert exc_info.value.args[0] == "Custom Error Message"
    assert exc_info.value.status_code == 400

# Test function to cover abort function with a status code that uses the default message
def test_abort_with_default_message(mocker):
    mocker.patch('sanic.exceptions._sanic_exceptions', _sanic_exceptions)
    
    with pytest.raises(SanicException) as exc_info:
        abort(404)
    
    default_message = STATUS_CODES[404].decode("utf8")
    assert exc_info.value.args[0] == default_message
    assert exc_info.value.status_code == 404

# Test function to cover abort function with a status code that is not in _sanic_exceptions
def test_abort_with_unmapped_status_code(mocker):
    mocker.patch('sanic.exceptions._sanic_exceptions', _sanic_exceptions)
    
    with pytest.raises(SanicException) as exc_info:
        abort(500)
    
    default_message = STATUS_CODES[500].decode("utf8")
    assert exc_info.value.args[0] == default_message
    assert exc_info.value.status_code == 500
