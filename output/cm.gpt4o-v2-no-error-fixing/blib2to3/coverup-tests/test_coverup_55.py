# file: src/blib2to3/pytree.py:593-638
# asked: {"lines": [611, 612, 613, 614, 615, 616, 617, 621, 622, 623, 638], "branches": [[611, 612], [611, 613], [613, 614], [613, 615], [621, 622], [621, 623]]}
# gained: {"lines": [611, 612, 613, 614, 615, 616, 617, 621, 622, 623, 638], "branches": [[611, 612], [611, 613], [613, 614], [613, 615], [621, 622], [621, 623]]}

import pytest
from blib2to3.pytree import LeafPattern, Leaf, BasePattern

class MockLeaf(Leaf):
    def __init__(self, value):
        self.value = value

class MockBasePattern(BasePattern):
    def match(self, node, results=None):
        return True

def test_leaf_pattern_init_with_type():
    pattern = LeafPattern(type=100)
    assert pattern.type == 100
    assert pattern.content is None
    assert pattern.name is None

def test_leaf_pattern_init_with_invalid_type():
    with pytest.raises(AssertionError):
        LeafPattern(type=300)

def test_leaf_pattern_init_with_content():
    pattern = LeafPattern(content="test")
    assert pattern.type is None
    assert pattern.content == "test"
    assert pattern.name is None

def test_leaf_pattern_init_with_invalid_content():
    with pytest.raises(AssertionError):
        LeafPattern(content=123)

def test_leaf_pattern_match_with_leaf(mocker):
    mocker.patch('blib2to3.pytree.BasePattern', MockBasePattern)
    pattern = LeafPattern()
    node = MockLeaf("value")
    assert pattern.match(node) is True

def test_leaf_pattern_match_with_non_leaf():
    pattern = LeafPattern()
    node = "not a leaf"
    assert pattern.match(node) is False

def test_leaf_pattern_submatch():
    pattern = LeafPattern(content="value")
    node = MockLeaf("value")
    assert pattern._submatch(node) is True

def test_leaf_pattern_submatch_no_match():
    pattern = LeafPattern(content="value")
    node = MockLeaf("different value")
    assert pattern._submatch(node) is False
