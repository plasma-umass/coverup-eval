# file: pymonet/maybe.py:101-112
# asked: {"lines": [101, 110, 111, 112], "branches": [[110, 111], [110, 112]]}
# gained: {"lines": [101, 110, 111, 112], "branches": [[110, 111], [110, 112]]}

import pytest
from pymonet.maybe import Maybe

def test_get_or_else_with_value():
    maybe = Maybe(10, False)
    assert maybe.get_or_else(20) == 10

def test_get_or_else_with_nothing():
    maybe = Maybe(None, True)
    assert maybe.get_or_else(20) == 20
