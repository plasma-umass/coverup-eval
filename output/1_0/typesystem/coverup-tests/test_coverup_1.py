# file typesystem/unique.py:4-14
# lines [4, 5, 12, 13]
# branches []

import pytest
from typesystem.unique import Uniqueness

def test_uniqueness_true_false_distinction():
    uniqueness = Uniqueness()
    assert uniqueness.TRUE is not True
    assert uniqueness.FALSE is not False
    assert uniqueness.TRUE != uniqueness.FALSE
