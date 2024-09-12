# file: pymonet/monad_try.py:10-12
# asked: {"lines": [10, 11, 12], "branches": []}
# gained: {"lines": [10, 11, 12], "branches": []}

import pytest
from pymonet.monad_try import Try

def test_try_success():
    t = Try(value=42, is_success=True)
    assert t.value == 42
    assert t.is_success is True

def test_try_failure():
    t = Try(value=Exception("error"), is_success=False)
    assert isinstance(t.value, Exception)
    assert str(t.value) == "error"
    assert t.is_success is False
