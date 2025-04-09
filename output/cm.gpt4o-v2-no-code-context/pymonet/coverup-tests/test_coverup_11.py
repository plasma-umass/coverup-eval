# file: pymonet/monad_try.py:53-64
# asked: {"lines": [53, 62, 63, 64], "branches": [[62, 63], [62, 64]]}
# gained: {"lines": [53, 62, 63, 64], "branches": [[62, 63], [62, 64]]}

import pytest
from pymonet.monad_try import Try

def test_try_bind_success(monkeypatch):
    class SuccessTry(Try):
        def __init__(self, value):
            self.value = value
            self.is_success = True

    def binder(value):
        return SuccessTry(value * 2)

    success_try = SuccessTry(10)
    result = success_try.bind(binder)
    
    assert isinstance(result, SuccessTry)
    assert result.value == 20

def test_try_bind_failure(monkeypatch):
    class FailureTry(Try):
        def __init__(self):
            self.is_success = False

    def binder(value):
        return FailureTry()

    failure_try = FailureTry()
    result = failure_try.bind(binder)
    
    assert isinstance(result, FailureTry)
    assert result.is_success == False
