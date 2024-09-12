# file: f100/__init__.py:1-3
# asked: {"lines": [1, 3], "branches": []}
# gained: {"lines": [1, 3], "branches": []}

import pytest
from f100 import make_a_pile

def test_make_a_pile():
    result = make_a_pile(3)
    assert result == [3, 5, 7]

    result = make_a_pile(0)
    assert result == []

    result = make_a_pile(1)
    assert result == [1]
