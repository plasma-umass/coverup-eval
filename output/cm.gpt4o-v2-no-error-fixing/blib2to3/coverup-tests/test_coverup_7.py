# file: src/blib2to3/pytree.py:396-419
# asked: {"lines": [396, 400, 401, 402, 411, 412, 413, 414, 415, 416, 417, 418, 419], "branches": [[412, 413], [412, 414], [416, 417], [416, 418]]}
# gained: {"lines": [396, 400, 401, 402, 411, 412, 413, 414, 415, 416, 417, 418, 419], "branches": [[412, 413], [412, 414], [416, 417], [416, 418]]}

import pytest
from blib2to3.pytree import Leaf, Context

def test_leaf_init_with_context():
    context = ("prefix", (10, 5))
    leaf = Leaf(type=100, value="value", context=context)
    
    assert leaf.type == 100
    assert leaf.value == "value"
    assert leaf._prefix == "prefix"
    assert leaf.lineno == 10
    assert leaf.column == 5
    assert leaf.fixers_applied == []
    assert leaf.children == []

def test_leaf_init_with_prefix():
    leaf = Leaf(type=100, value="value", prefix="prefix")
    
    assert leaf.type == 100
    assert leaf.value == "value"
    assert leaf._prefix == "prefix"
    assert leaf.fixers_applied == []
    assert leaf.children == []

def test_leaf_init_with_fixers_applied():
    fixers = ["fixer1", "fixer2"]
    leaf = Leaf(type=100, value="value", fixers_applied=fixers)
    
    assert leaf.type == 100
    assert leaf.value == "value"
    assert leaf.fixers_applied == fixers
    assert leaf.children == []

def test_leaf_init_type_assertion():
    with pytest.raises(AssertionError):
        Leaf(type=300, value="value")
