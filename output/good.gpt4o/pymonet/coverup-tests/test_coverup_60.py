# file pymonet/monad_try.py:10-12
# lines [10, 11, 12]
# branches []

import pytest
from pymonet.monad_try import Try

def test_try_initialization():
    # Test successful Try
    success_try = Try(value=42, is_success=True)
    assert success_try.value == 42
    assert success_try.is_success is True

    # Test failed Try
    failure_try = Try(value=Exception("error"), is_success=False)
    assert isinstance(failure_try.value, Exception)
    assert failure_try.value.args[0] == "error"
    assert failure_try.is_success is False
