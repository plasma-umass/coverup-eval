# file src/blib2to3/pytree.py:396-419
# lines [396, 400, 401, 402, 411, 412, 413, 414, 415, 416, 417, 418, 419]
# branches ['412->413', '412->414', '416->417', '416->418']

import pytest
from blib2to3.pytree import Leaf

def test_leaf_initialization():
    # Test with all parameters
    leaf = Leaf(type=100, value="test_value", context=(("prefix", (1, 2))), prefix="test_prefix", fixers_applied=["fixer1"])
    assert leaf.type == 100
    assert leaf.value == "test_value"
    assert leaf._prefix == "test_prefix"
    assert leaf.lineno == 1
    assert leaf.column == 2
    assert leaf.fixers_applied == ["fixer1"]
    assert leaf.children == []

    # Test with minimal parameters
    leaf = Leaf(type=100, value="test_value")
    assert leaf.type == 100
    assert leaf.value == "test_value"
    assert leaf._prefix == ""
    assert leaf.lineno == 0
    assert leaf.column == 0
    assert leaf.fixers_applied == []
    assert leaf.children == []

    # Test with context but no prefix
    leaf = Leaf(type=100, value="test_value", context=(("prefix", (1, 2))))
    assert leaf.type == 100
    assert leaf.value == "test_value"
    assert leaf._prefix == "prefix"
    assert leaf.lineno == 1
    assert leaf.column == 2
    assert leaf.fixers_applied == []
    assert leaf.children == []

    # Test with prefix but no context
    leaf = Leaf(type=100, value="test_value", prefix="test_prefix")
    assert leaf.type == 100
    assert leaf.value == "test_value"
    assert leaf._prefix == "test_prefix"
    assert leaf.lineno == 0
    assert leaf.column == 0
    assert leaf.fixers_applied == []
    assert leaf.children == []

    # Test with invalid type
    with pytest.raises(AssertionError):
        Leaf(type=300, value="test_value")

@pytest.fixture(autouse=True)
def cleanup(mocker):
    # Cleanup code to ensure no side effects
    mocker.stopall()
