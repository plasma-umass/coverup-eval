# file: pymonet/monad_try.py:10-12
# asked: {"lines": [10, 11, 12], "branches": []}
# gained: {"lines": [10, 11, 12], "branches": []}

import pytest
from pymonet.monad_try import Try

def test_try_init():
    # Test initialization with success
    success_try = Try(value="Success", is_success=True)
    assert success_try.value == "Success"
    assert success_try.is_success is True

    # Test initialization with failure
    failure_try = Try(value="Failure", is_success=False)
    assert failure_try.value == "Failure"
    assert failure_try.is_success is False
