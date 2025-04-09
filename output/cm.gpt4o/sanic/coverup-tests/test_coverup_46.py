# file sanic/exceptions.py:146-152
# lines [146, 147, 148, 152]
# branches []

import pytest
from sanic.exceptions import SanicException, add_status_code

@add_status_code(417)
class HeaderExpectationFailed(SanicException):
    """
    **Status**: 417 Expectation Failed
    """
    pass

def test_header_expectation_failed():
    try:
        raise HeaderExpectationFailed("Expectation Failed")
    except HeaderExpectationFailed as e:
        assert e.status_code == 417
        assert str(e) == "Expectation Failed"
