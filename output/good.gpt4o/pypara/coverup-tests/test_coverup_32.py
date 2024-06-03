# file pypara/monetary.py:48-53
# lines [48, 49, 53]
# branches []

import pytest
from pypara.monetary import MonetaryOperationException

def test_monetary_operation_exception():
    with pytest.raises(MonetaryOperationException):
        raise MonetaryOperationException("This operation cannot be carried out")

    # Ensure the exception message is correct
    try:
        raise MonetaryOperationException("This operation cannot be carried out")
    except MonetaryOperationException as e:
        assert str(e) == "This operation cannot be carried out"
