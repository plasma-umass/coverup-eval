# file: pypara/monetary.py:48-53
# asked: {"lines": [48, 49, 53], "branches": []}
# gained: {"lines": [48, 49, 53], "branches": []}

import pytest
from pypara.monetary import MonetaryOperationException

def test_monetary_operation_exception():
    with pytest.raises(MonetaryOperationException):
        raise MonetaryOperationException("Operation not allowed")
