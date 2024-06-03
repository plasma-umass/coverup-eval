# file sanic/exceptions.py:24-33
# lines [24, 25, 26, 28, 29, 32, 33]
# branches ['28->29', '28->32', '32->exit', '32->33']

import pytest
from sanic.exceptions import SanicException

def test_sanic_exception_status_code_and_quiet():
    # Test with status_code and quiet=None
    exc = SanicException("Test message", status_code=404, quiet=None)
    assert exc.status_code == 404
    assert exc.quiet is True

    # Test with status_code and quiet=False
    exc = SanicException("Test message", status_code=404, quiet=False)
    assert exc.status_code == 404
    assert not hasattr(exc, 'quiet')

    # Test with status_code=500 and quiet=None
    exc = SanicException("Test message", status_code=500, quiet=None)
    assert exc.status_code == 500
    assert not hasattr(exc, 'quiet')

    # Test with status_code=None and quiet=None
    exc = SanicException("Test message", status_code=None, quiet=None)
    assert not hasattr(exc, 'status_code')
    assert not hasattr(exc, 'quiet')

    # Test with status_code=None and quiet=True
    exc = SanicException("Test message", status_code=None, quiet=True)
    assert not hasattr(exc, 'status_code')
    assert exc.quiet is True

    # Test with status_code=500 and quiet=True
    exc = SanicException("Test message", status_code=500, quiet=True)
    assert exc.status_code == 500
    assert exc.quiet is True
