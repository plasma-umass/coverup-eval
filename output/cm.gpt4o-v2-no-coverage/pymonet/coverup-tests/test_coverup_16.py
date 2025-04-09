# file: pymonet/monad_try.py:53-64
# asked: {"lines": [53, 62, 63, 64], "branches": [[62, 63], [62, 64]]}
# gained: {"lines": [53, 62, 63, 64], "branches": [[62, 63], [62, 64]]}

import pytest
from pymonet.monad_try import Try

def test_try_bind_success():
    def binder(x):
        return Try(x + 1, True)

    t = Try(1, True)
    result = t.bind(binder)
    assert result.value == 2
    assert result.is_success

def test_try_bind_failure():
    def binder(x):
        return Try(x + 1, True)

    t = Try(1, False)
    result = t.bind(binder)
    assert result.value == 1
    assert not result.is_success
