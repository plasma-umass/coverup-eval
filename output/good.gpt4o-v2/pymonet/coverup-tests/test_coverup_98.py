# file: pymonet/either.py:106-111
# asked: {"lines": [106, 111], "branches": []}
# gained: {"lines": [106, 111], "branches": []}

import pytest
from pymonet.either import Left, Either

def test_left_ap():
    left_instance = Left("error")
    result = left_instance.ap(None)
    assert isinstance(result, Left)
    assert result.value == "error"
