# file: src/blib2to3/pytree.py:593-638
# asked: {"lines": [593, 594, 596, 597, 598, 611, 612, 613, 614, 615, 616, 617, 619, 621, 622, 623, 625, 638], "branches": [[611, 612], [611, 613], [613, 614], [613, 615], [621, 622], [621, 623]]}
# gained: {"lines": [593, 594, 596, 597, 598, 611, 612, 613, 614, 615, 616, 617, 619, 621, 622, 623, 625, 638], "branches": [[611, 612], [611, 613], [613, 614], [613, 615], [621, 622], [621, 623]]}

import pytest
from blib2to3.pytree import LeafPattern, BasePattern, Leaf

class MockLeaf(Leaf):
    def __init__(self, type, value):
        self.type = type
        self.value = value

class MockBasePattern(BasePattern):
    def match(self, node, results=None):
        return True

@pytest.fixture
def mock_leaf():
    return MockLeaf(type=1, value="test")

@pytest.fixture
def mock_base_pattern(monkeypatch):
    monkeypatch.setattr(LeafPattern, "match", MockBasePattern().match)

def test_leaf_pattern_init_type():
    pattern = LeafPattern(type=100)
    assert pattern.type == 100
    assert pattern.content is None
    assert pattern.name is None

def test_leaf_pattern_init_content():
    pattern = LeafPattern(content="test")
    assert pattern.type is None
    assert pattern.content == "test"
    assert pattern.name is None

def test_leaf_pattern_init_name():
    pattern = LeafPattern(name="test_name")
    assert pattern.type is None
    assert pattern.content is None
    assert pattern.name == "test_name"

def test_leaf_pattern_init_invalid_type():
    with pytest.raises(AssertionError):
        LeafPattern(type=300)

def test_leaf_pattern_init_invalid_content():
    with pytest.raises(AssertionError):
        LeafPattern(content=123)

def test_leaf_pattern_match_leaf(mock_leaf):
    pattern = LeafPattern(type=1, content="test")
    assert pattern.match(mock_leaf)

def test_leaf_pattern_match_non_leaf():
    pattern = LeafPattern(type=1, content="test")
    assert not pattern.match("not_a_leaf")

def test_leaf_pattern_submatch_true(mock_leaf):
    pattern = LeafPattern(type=1, content="test")
    assert pattern._submatch(mock_leaf)

def test_leaf_pattern_submatch_false(mock_leaf):
    pattern = LeafPattern(type=1, content="not_test")
    assert not pattern._submatch(mock_leaf)

def test_leaf_pattern_match_with_results(mock_leaf, mock_base_pattern):
    pattern = LeafPattern(type=1, content="test")
    results = {}
    assert pattern.match(mock_leaf, results)
    assert results == {}

def test_leaf_pattern_submatch_with_results(mock_leaf):
    pattern = LeafPattern(type=1, content="test")
    results = {}
    assert pattern._submatch(mock_leaf, results)
    assert results == {}
