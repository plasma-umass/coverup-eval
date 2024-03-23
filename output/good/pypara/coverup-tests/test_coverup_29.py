# file pypara/monetary.py:48-53
# lines [48, 49, 53]
# branches []

import pytest
from pypara.monetary import MonetaryOperationException

def test_monetary_operation_exception():
    with pytest.raises(MonetaryOperationException) as exc_info:
        raise MonetaryOperationException("Test exception")

    assert str(exc_info.value) == "Test exception"
