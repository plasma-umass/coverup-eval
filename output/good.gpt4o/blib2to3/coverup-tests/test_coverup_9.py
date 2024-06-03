# file src/blib2to3/pytree.py:593-638
# lines [593, 594, 596, 597, 598, 611, 612, 613, 614, 615, 616, 617, 619, 621, 622, 623, 625, 638]
# branches ['611->612', '611->613', '613->614', '613->615', '621->622', '621->623']

import pytest
from blib2to3.pytree import Leaf, BasePattern

class TestLeafPattern:
    def test_leaf_pattern_init(self):
        from blib2to3.pytree import LeafPattern

        # Test with type, content, and name
        pattern = LeafPattern(type=100, content="test", name="test_name")
        assert pattern.type == 100
        assert pattern.content == "test"
        assert pattern.name == "test_name"

        # Test with only type
        pattern = LeafPattern(type=200)
        assert pattern.type == 200
        assert pattern.content is None
        assert pattern.name is None

        # Test with only content
        pattern = LeafPattern(content="test_content")
        assert pattern.type is None
        assert pattern.content == "test_content"
        assert pattern.name is None

        # Test with only name
        pattern = LeafPattern(name="test_name")
        assert pattern.type is None
        assert pattern.content is None
        assert pattern.name == "test_name"

        # Test with no arguments
        pattern = LeafPattern()
        assert pattern.type is None
        assert pattern.content is None
        assert pattern.name is None

        # Test invalid type
        with pytest.raises(AssertionError):
            LeafPattern(type=300)

        # Test invalid content
        with pytest.raises(AssertionError):
            LeafPattern(content=123)

    def test_leaf_pattern_match(self, mocker):
        from blib2to3.pytree import LeafPattern

        pattern = LeafPattern(type=100, content="test", name="test_name")

        # Mock a Leaf node
        mock_leaf = mocker.Mock(spec=Leaf)
        mock_leaf.type = 100
        mock_leaf.value = "test"

        # Test match with a Leaf node
        assert pattern.match(mock_leaf)

        # Mock a non-Leaf node
        mock_non_leaf = mocker.Mock()
        assert not pattern.match(mock_non_leaf)

    def test_leaf_pattern_submatch(self, mocker):
        from blib2to3.pytree import LeafPattern

        pattern = LeafPattern(type=100, content="test", name="test_name")

        # Mock a Leaf node
        mock_leaf = mocker.Mock(spec=Leaf)
        mock_leaf.type = 100
        mock_leaf.value = "test"

        # Test _submatch with matching content
        assert pattern._submatch(mock_leaf)

        # Test _submatch with non-matching content
        mock_leaf.value = "non_matching"
        assert not pattern._submatch(mock_leaf)
