# file: src/blib2to3/pytree.py:396-419
# asked: {"lines": [396, 400, 401, 402, 411, 412, 413, 414, 415, 416, 417, 418, 419], "branches": [[412, 413], [412, 414], [416, 417], [416, 418]]}
# gained: {"lines": [396, 400, 401, 402, 411, 412, 413, 414, 415, 416, 417, 418, 419], "branches": [[412, 413], [412, 414], [416, 417], [416, 418]]}

import pytest
from blib2to3.pytree import Leaf

def test_leaf_initialization_with_context():
    context = (" ", (1, 2))
    leaf = Leaf(type=100, value="test", context=context)
    assert leaf.type == 100
    assert leaf.value == "test"
    assert leaf._prefix == " "
    assert leaf.lineno == 1
    assert leaf.column == 2
    assert leaf.fixers_applied == []
    assert leaf.children == []

def test_leaf_initialization_with_prefix():
    leaf = Leaf(type=100, value="test", prefix="prefix_")
    assert leaf.type == 100
    assert leaf.value == "test"
    assert leaf._prefix == "prefix_"
    assert leaf.fixers_applied == []
    assert leaf.children == []

def test_leaf_initialization_with_fixers_applied():
    fixers = ["fixer1", "fixer2"]
    leaf = Leaf(type=100, value="test", fixers_applied=fixers)
    assert leaf.type == 100
    assert leaf.value == "test"
    assert leaf.fixers_applied == fixers
    assert leaf.children == []

def test_leaf_initialization_type_assertion():
    with pytest.raises(AssertionError):
        Leaf(type=300, value="test")

@pytest.fixture(autouse=True)
def run_around_tests(monkeypatch):
    # Setup: Ensure no state pollution
    yield
    # Teardown: Clean up any state if necessary
    monkeypatch.undo()
