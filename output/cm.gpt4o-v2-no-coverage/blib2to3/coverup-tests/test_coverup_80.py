# file: src/blib2to3/pytree.py:593-638
# asked: {"lines": [611, 612, 613, 614, 615, 616, 617, 621, 622, 623, 638], "branches": [[611, 612], [611, 613], [613, 614], [613, 615], [621, 622], [621, 623]]}
# gained: {"lines": [611, 612, 613, 614, 615, 616, 617, 621, 622, 623, 638], "branches": [[611, 612], [611, 613], [613, 614], [613, 615], [621, 622], [621, 623]]}

import pytest
from blib2to3.pytree import LeafPattern, BasePattern, Leaf
from typing import Optional, Text

class TestLeafPattern:
    def test_init_with_type(self):
        pattern = LeafPattern(type=100)
        assert pattern.type == 100
        assert pattern.content is None
        assert pattern.name is None

    def test_init_with_content(self):
        pattern = LeafPattern(content="test")
        assert pattern.type is None
        assert pattern.content == "test"
        assert pattern.name is None

    def test_init_with_name(self):
        pattern = LeafPattern(name="test_name")
        assert pattern.type is None
        assert pattern.content is None
        assert pattern.name == "test_name"

    def test_init_with_all_params(self):
        pattern = LeafPattern(type=100, content="test", name="test_name")
        assert pattern.type == 100
        assert pattern.content == "test"
        assert pattern.name == "test_name"

    def test_init_invalid_type(self):
        with pytest.raises(AssertionError):
            LeafPattern(type=300)

    def test_init_invalid_content(self):
        with pytest.raises(AssertionError):
            LeafPattern(content=123)

    def test_match_leaf_node(self, mocker):
        mocker.patch('blib2to3.pytree.BasePattern.match', return_value=True)
        leaf = Leaf(type=1, value="value")
        pattern = LeafPattern(type=1, content="value")
        assert pattern.match(leaf) is True

    def test_match_non_leaf_node(self):
        class NonLeaf:
            pass
        pattern = LeafPattern()
        assert pattern.match(NonLeaf()) is False

    def test_submatch(self):
        leaf = Leaf(type=1, value="value")
        pattern = LeafPattern(content="value")
        assert pattern._submatch(leaf) is True

    def test_submatch_no_content(self):
        leaf = Leaf(type=1, value="value")
        pattern = LeafPattern()
        assert pattern._submatch(leaf) is False
