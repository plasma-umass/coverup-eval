# file sanic/exceptions.py:118-124
# lines [118, 119, 120, 124]
# branches []

import pytest
from sanic.exceptions import PayloadTooLarge, SanicException, add_status_code

# Assuming the add_status_code decorator is defined elsewhere in sanic.exceptions
# and works as intended, we don't need to redefine it here.

# Test function to cover PayloadTooLarge exception
def test_payload_too_large_exception():
    with pytest.raises(PayloadTooLarge) as exc_info:
        raise PayloadTooLarge("Payload too large")

    assert exc_info.value.status_code == 413
    assert str(exc_info.value) == "Payload too large"
