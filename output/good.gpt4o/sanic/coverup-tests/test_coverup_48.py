# file sanic/exceptions.py:118-124
# lines [118, 119, 120, 124]
# branches []

import pytest
from sanic.exceptions import SanicException, add_status_code

def test_payload_too_large_exception():
    @add_status_code(413)
    class PayloadTooLarge(SanicException):
        """
        **Status**: 413 Payload Too Large
        """
        pass

    exception = PayloadTooLarge("Payload is too large")
    assert isinstance(exception, SanicException)
    assert exception.status_code == 413
    assert str(exception) == "Payload is too large"
