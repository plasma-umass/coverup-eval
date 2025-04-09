# file: pymonet/maybe.py:14-17
# asked: {"lines": [14, 15, 16, 17], "branches": [[16, 0], [16, 17]]}
# gained: {"lines": [14, 15, 16, 17], "branches": [[16, 0], [16, 17]]}

import pytest
from pymonet.maybe import Maybe

def test_maybe_init_with_value():
    maybe = Maybe(10, False)
    assert maybe.is_nothing is False
    assert maybe.value == 10

def test_maybe_init_with_nothing():
    maybe = Maybe(None, True)
    assert maybe.is_nothing is True
    assert not hasattr(maybe, 'value')
