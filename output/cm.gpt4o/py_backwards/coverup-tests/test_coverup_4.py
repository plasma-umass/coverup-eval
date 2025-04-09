# file py_backwards/transformers/six_moves.py:7-18
# lines [7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18]
# branches ['10->11', '10->12', '13->14', '13->18', '14->15', '14->17']

import pytest
from py_backwards.transformers.six_moves import MovedAttribute

def test_moved_attribute_initialization():
    # Test case where new_mod is None
    attr = MovedAttribute(name="test_name", old_mod="old_module", new_mod=None)
    assert attr.name == "test_name"
    assert attr.new_mod == "test_name"
    assert attr.new_attr == "test_name"

    # Test case where new_attr is None and old_attr is provided
    attr = MovedAttribute(name="test_name", old_mod="old_module", new_mod="new_module", old_attr="old_attribute")
    assert attr.name == "test_name"
    assert attr.new_mod == "new_module"
    assert attr.new_attr == "old_attribute"

    # Test case where both new_attr and old_attr are None
    attr = MovedAttribute(name="test_name", old_mod="old_module", new_mod="new_module")
    assert attr.name == "test_name"
    assert attr.new_mod == "new_module"
    assert attr.new_attr == "test_name"

    # Test case where new_attr is provided
    attr = MovedAttribute(name="test_name", old_mod="old_module", new_mod="new_module", new_attr="new_attribute")
    assert attr.name == "test_name"
    assert attr.new_mod == "new_module"
    assert attr.new_attr == "new_attribute"
