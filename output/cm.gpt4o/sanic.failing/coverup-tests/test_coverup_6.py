# file sanic/exceptions.py:24-33
# lines [24, 25, 26, 28, 29, 32, 33]
# branches ['28->29', '28->32', '32->exit', '32->33']

import pytest
from sanic.exceptions import SanicException

def test_sanic_exception_status_code():
    # Test with status_code provided
    exc = SanicException("Test message", status_code=404)
    assert exc.status_code == 404

def test_sanic_exception_quiet_true():
    # Test with quiet=True
    exc = SanicException("Test message", quiet=True)
    assert exc.quiet is True

def test_sanic_exception_quiet_none_status_code_500():
    # Test with quiet=None and status_code=500
    exc = SanicException("Test message", status_code=500)
    assert not hasattr(exc, 'quiet')

def test_sanic_exception_quiet_none_status_code_not_500():
    # Test with quiet=None and status_code not 500
    exc = SanicException("Test message", status_code=404)
    assert exc.quiet is True

def test_sanic_exception_quiet_false():
    # Test with quiet=False
    exc = SanicException("Test message", quiet=False)
    assert not hasattr(exc, 'quiet')
