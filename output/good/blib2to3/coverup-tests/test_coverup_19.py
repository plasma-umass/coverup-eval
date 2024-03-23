# file src/blib2to3/pytree.py:885-900
# lines [885, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900]
# branches ['891->892', '891->898', '893->891', '893->894', '894->893', '894->895']

import pytest
from blib2to3.pytree import WildcardPattern, LeafPattern
from blib2to3.pgen2.token import NAME

class TestWildcardPattern:
    @pytest.fixture
    def leaf_pattern(self, mocker):
        # Mock a LeafPattern that always matches and increments the match count
        mock_leaf_pattern = mocker.Mock(spec=LeafPattern)
        mock_leaf_pattern.match.side_effect = lambda node, results: True
        return mock_leaf_pattern

    def test_bare_name_matches(self, leaf_pattern, mocker):
        # Create a WildcardPattern with mocked LeafPattern content
        wildcard_pattern = WildcardPattern(content=[(leaf_pattern, None)], name='wildcard')

        # Create dummy nodes to match against
        nodes = [mocker.Mock() for _ in range(3)]

        # Call the _bare_name_matches method
        count, results = wildcard_pattern._bare_name_matches(nodes)

        # Assert that all nodes were matched
        assert count == len(nodes)
        assert results['wildcard'] == nodes

        # Assert that the leaf pattern match was called the correct number of times
        assert leaf_pattern.match.call_count == len(nodes)

        # Clean up by removing the side effect
        leaf_pattern.match.side_effect = None
