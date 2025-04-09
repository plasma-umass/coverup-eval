# file src/blib2to3/pytree.py:396-419
# lines [396, 400, 401, 402, 411, 412, 413, 414, 415, 416, 417, 418, 419]
# branches ['412->413', '412->414', '416->417', '416->418']

import pytest
from blib2to3.pytree import Leaf

def test_leaf_initialization_with_context_and_prefix():
    # Test initialization with context and prefix
    leaf = Leaf(type=255, value="test", context=("", (1, 0)), prefix=" ")
    assert leaf._prefix == " "
    assert leaf.lineno == 1
    assert leaf.column == 0
    assert leaf.type == 255
    assert leaf.value == "test"
    assert leaf.fixers_applied == []
    assert leaf.children == []

def test_leaf_initialization_with_context_without_prefix():
    # Test initialization with context but without prefix
    leaf = Leaf(type=255, value="test", context=("#", (2, 1)))
    assert leaf._prefix == "#"
    assert leaf.lineno == 2
    assert leaf.column == 1
    assert leaf.type == 255
    assert leaf.value == "test"
    assert leaf.fixers_applied == []
    assert leaf.children == []

def test_leaf_initialization_without_context_with_prefix():
    # Test initialization without context but with prefix
    leaf = Leaf(type=255, value="test", prefix=" ")
    assert leaf._prefix == " "
    assert leaf.type == 255
    assert leaf.value == "test"
    assert leaf.fixers_applied == []
    assert leaf.children == []

def test_leaf_initialization_without_context_and_prefix():
    # Test initialization without context and without prefix
    leaf = Leaf(type=255, value="test")
    assert leaf.type == 255
    assert leaf.value == "test"
    assert leaf.fixers_applied == []
    assert leaf.children == []

def test_leaf_initialization_with_fixers_applied():
    # Test initialization with fixers_applied
    fixers = ['fixer1', 'fixer2']
    leaf = Leaf(type=255, value="test", fixers_applied=fixers)
    assert leaf.fixers_applied == fixers
    assert leaf.fixers_applied is not fixers  # Ensure it's a copy
    assert leaf.type == 255
    assert leaf.value == "test"
    assert leaf.children == []

def test_leaf_initialization_type_assertion():
    # Test that the type assertion works
    with pytest.raises(AssertionError):
        Leaf(type=256, value="test")
