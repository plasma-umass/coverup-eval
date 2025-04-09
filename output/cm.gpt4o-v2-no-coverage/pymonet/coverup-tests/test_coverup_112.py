# file: pymonet/monad_try.py:107-114
# asked: {"lines": [107, 114], "branches": []}
# gained: {"lines": [107, 114], "branches": []}

import pytest
from pymonet.monad_try import Try

def test_try_get():
    # Test for successful Try
    success_try = Try(value=42, is_success=True)
    assert success_try.get() == 42

    # Test for failed Try
    fail_try = Try(value="error", is_success=False)
    assert fail_try.get() == "error"
