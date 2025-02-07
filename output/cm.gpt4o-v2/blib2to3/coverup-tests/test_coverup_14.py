# file: src/blib2to3/pytree.py:593-638
# asked: {"lines": [593, 594, 596, 597, 598, 611, 612, 613, 614, 615, 616, 617, 619, 621, 622, 623, 625, 638], "branches": [[611, 612], [611, 613], [613, 614], [613, 615], [621, 622], [621, 623]]}
# gained: {"lines": [593, 594, 596, 597, 598, 611, 612, 613, 614, 615, 616, 617, 619, 621, 622, 623, 625, 638], "branches": [[611, 612], [611, 613], [613, 614], [613, 615], [621, 622], [621, 623]]}

import pytest
from blib2to3.pytree import LeafPattern, BasePattern, Leaf

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

    def test_init_with_all(self):
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
        mock_node = mocker.Mock(spec=Leaf)
        pattern = LeafPattern()
        assert pattern.match(mock_node) is True

    def test_match_non_leaf_node(self, mocker):
        mock_node = mocker.Mock()
        pattern = LeafPattern()
        assert pattern.match(mock_node) is False

    def test_submatch_content_match(self, mocker):
        mock_node = mocker.Mock()
        mock_node.value = "test"
        pattern = LeafPattern(content="test")
        assert pattern._submatch(mock_node) is True

    def test_submatch_content_no_match(self, mocker):
        mock_node = mocker.Mock()
        mock_node.value = "no_match"
        pattern = LeafPattern(content="test")
        assert pattern._submatch(mock_node) is False
