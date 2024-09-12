# file: typesystem/unique.py:15-18
# asked: {"lines": [15, 16, 17, 18], "branches": [[17, 0], [17, 18]]}
# gained: {"lines": [15, 16, 17, 18], "branches": [[17, 0], [17, 18]]}

import pytest
from typesystem.unique import Uniqueness

def test_uniqueness_init_with_items():
    items = [1, 2, 3]
    uniqueness = Uniqueness(items)
    for item in items:
        assert item in uniqueness._set

def test_uniqueness_init_without_items():
    uniqueness = Uniqueness()
    assert len(uniqueness._set) == 0
