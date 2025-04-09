# file: pymonet/maybe.py:35-42
# asked: {"lines": [35, 36, 42], "branches": []}
# gained: {"lines": [35, 36, 42], "branches": []}

import pytest
from pymonet.maybe import Maybe

def test_maybe_nothing():
    nothing = Maybe.nothing()
    assert nothing.is_nothing
    assert not hasattr(nothing, 'value')
