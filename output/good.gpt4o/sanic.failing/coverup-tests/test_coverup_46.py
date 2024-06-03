# file sanic/exceptions.py:146-152
# lines [146, 147, 148, 152]
# branches []

import pytest
from sanic.exceptions import SanicException, add_status_code

def test_header_expectation_failed():
    @add_status_code(417)
    class HeaderExpectationFailed(SanicException):
        """
        **Status**: 417 Expectation Failed
        """
        pass

    exception_instance = HeaderExpectationFailed("Expectation Failed")
    
    assert isinstance(exception_instance, SanicException)
    assert exception_instance.status_code == 417
    assert str(exception_instance) == "Expectation Failed"
