# file: py_backwards/transformers/six_moves.py:7-18
# asked: {"lines": [7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18], "branches": [[10, 11], [10, 12], [13, 14], [13, 18], [14, 15], [14, 17]]}
# gained: {"lines": [7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18], "branches": [[10, 11], [10, 12], [13, 14], [13, 18], [14, 15], [14, 17]]}

import pytest
from py_backwards.transformers.six_moves import MovedAttribute

def test_moved_attribute_new_mod_none():
    attr = MovedAttribute(name="test_name", old_mod="old_module", new_mod=None)
    assert attr.new_mod == "test_name"
    assert attr.new_attr == "test_name"

def test_moved_attribute_new_attr_none_old_attr_none():
    attr = MovedAttribute(name="test_name", old_mod="old_module", new_mod="new_module", old_attr=None, new_attr=None)
    assert attr.new_attr == "test_name"

def test_moved_attribute_new_attr_none_old_attr_not_none():
    attr = MovedAttribute(name="test_name", old_mod="old_module", new_mod="new_module", old_attr="old_attr", new_attr=None)
    assert attr.new_attr == "old_attr"
