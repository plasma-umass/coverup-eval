# file: py_backwards/transformers/six_moves.py:7-18
# asked: {"lines": [7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18], "branches": [[10, 11], [10, 12], [13, 14], [13, 18], [14, 15], [14, 17]]}
# gained: {"lines": [7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18], "branches": [[10, 11], [10, 12], [13, 14], [13, 18], [14, 15], [14, 17]]}

import pytest
from py_backwards.transformers.six_moves import MovedAttribute

def test_moved_attribute_initialization():
    # Test case where all attributes are provided
    attr = MovedAttribute(name="test", old_mod="old_module", new_mod="new_module", old_attr="old_attr", new_attr="new_attr")
    assert attr.name == "test"
    assert attr.new_mod == "new_module"
    assert attr.new_attr == "new_attr"

    # Test case where new_mod is None
    attr = MovedAttribute(name="test", old_mod="old_module", new_mod=None, old_attr="old_attr", new_attr="new_attr")
    assert attr.name == "test"
    assert attr.new_mod == "test"
    assert attr.new_attr == "new_attr"

    # Test case where new_attr is None and old_attr is provided
    attr = MovedAttribute(name="test", old_mod="old_module", new_mod="new_module", old_attr="old_attr", new_attr=None)
    assert attr.name == "test"
    assert attr.new_mod == "new_module"
    assert attr.new_attr == "old_attr"

    # Test case where new_attr and old_attr are None
    attr = MovedAttribute(name="test", old_mod="old_module", new_mod="new_module", old_attr=None, new_attr=None)
    assert attr.name == "test"
    assert attr.new_mod == "new_module"
    assert attr.new_attr == "test"

    # Test case where new_mod and new_attr are None, old_attr is provided
    attr = MovedAttribute(name="test", old_mod="old_module", new_mod=None, old_attr="old_attr", new_attr=None)
    assert attr.name == "test"
    assert attr.new_mod == "test"
    assert attr.new_attr == "old_attr"

    # Test case where new_mod and new_attr are None, old_attr is None
    attr = MovedAttribute(name="test", old_mod="old_module", new_mod=None, old_attr=None, new_attr=None)
    assert attr.name == "test"
    assert attr.new_mod == "test"
    assert attr.new_attr == "test"
