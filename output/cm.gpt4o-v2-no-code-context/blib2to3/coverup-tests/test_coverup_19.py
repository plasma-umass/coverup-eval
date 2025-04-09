# file: src/blib2to3/pytree.py:593-638
# asked: {"lines": [593, 594, 596, 597, 598, 611, 612, 613, 614, 615, 616, 617, 619, 621, 622, 623, 625, 638], "branches": [[611, 612], [611, 613], [613, 614], [613, 615], [621, 622], [621, 623]]}
# gained: {"lines": [593, 594, 596, 597, 598, 611, 612, 613, 614, 615, 616, 617, 619, 621, 622, 623, 625, 638], "branches": [[611, 612], [611, 613], [613, 614], [613, 615], [621, 622], [621, 623]]}

import pytest
from blib2to3.pytree import LeafPattern, Leaf, BasePattern

def test_leaf_pattern_init_with_type():
    pattern = LeafPattern(type=100)
    assert pattern.type == 100
    assert pattern.content is None
    assert pattern.name is None

def test_leaf_pattern_init_with_content():
    pattern = LeafPattern(content="test")
    assert pattern.type is None
    assert pattern.content == "test"
    assert pattern.name is None

def test_leaf_pattern_init_with_name():
    pattern = LeafPattern(name="test_name")
    assert pattern.type is None
    assert pattern.content is None
    assert pattern.name == "test_name"

def test_leaf_pattern_init_with_all_params():
    pattern = LeafPattern(type=100, content="test", name="test_name")
    assert pattern.type == 100
    assert pattern.content == "test"
    assert pattern.name == "test_name"

def test_leaf_pattern_match_with_leaf(mocker):
    mock_leaf = mocker.Mock(spec=Leaf)
    pattern = LeafPattern()
    assert pattern.match(mock_leaf) is True

def test_leaf_pattern_match_with_non_leaf(mocker):
    mock_node = mocker.Mock(spec=BasePattern)
    pattern = LeafPattern()
    assert pattern.match(mock_node) is False

def test_leaf_pattern_submatch_with_matching_content(mocker):
    mock_leaf = mocker.Mock(spec=Leaf)
    mock_leaf.value = "test"
    pattern = LeafPattern(content="test")
    assert pattern._submatch(mock_leaf) is True

def test_leaf_pattern_submatch_with_non_matching_content(mocker):
    mock_leaf = mocker.Mock(spec=Leaf)
    mock_leaf.value = "not_test"
    pattern = LeafPattern(content="test")
    assert pattern._submatch(mock_leaf) is False
