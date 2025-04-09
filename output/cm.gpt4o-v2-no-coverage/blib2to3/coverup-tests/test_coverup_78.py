# file: src/blib2to3/pytree.py:856-883
# asked: {"lines": [858, 859, 860, 862, 864, 865, 866, 867, 870, 871, 872, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883], "branches": [[859, 860], [859, 862], [864, 865], [864, 870], [865, 864], [865, 866], [870, 0], [870, 871], [872, 874], [872, 883], [874, 872], [874, 875], [875, 872], [875, 876], [876, 875], [876, 877], [877, 876], [877, 878]]}
# gained: {"lines": [858, 859, 860, 862, 864, 865, 866, 867, 870, 871, 872, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883], "branches": [[859, 860], [864, 865], [864, 870], [865, 864], [865, 866], [870, 0], [870, 871], [872, 874], [872, 883], [874, 872], [874, 875], [875, 872], [875, 876], [876, 875], [876, 877], [877, 878]]}

import pytest
from unittest.mock import MagicMock

class TestWildcardPattern:
    @pytest.fixture
    def setup_wildcard_pattern(self):
        from blib2to3.pytree import WildcardPattern, BasePattern

        class MockPattern(BasePattern):
            def generate_matches(self, nodes):
                yield (1, {'mock': 'result'})

        wildcard_pattern = WildcardPattern(content=[[MockPattern()]])
        wildcard_pattern.min = 0
        wildcard_pattern.max = 2

        return wildcard_pattern

    def test_iterative_matches_min_zero(self, setup_wildcard_pattern):
        wildcard_pattern = setup_wildcard_pattern
        nodes = ['node1', 'node2']

        matches = list(wildcard_pattern._iterative_matches(nodes))
        assert matches[0] == (0, {})

    def test_iterative_matches_generate_matches(self, setup_wildcard_pattern):
        wildcard_pattern = setup_wildcard_pattern
        nodes = ['node1', 'node2']

        matches = list(wildcard_pattern._iterative_matches(nodes))
        assert (1, {'mock': 'result'}) in matches

    def test_iterative_matches_iterate_down_nodes(self, setup_wildcard_pattern):
        wildcard_pattern = setup_wildcard_pattern
        nodes = ['node1', 'node2']

        matches = list(wildcard_pattern._iterative_matches(nodes))
        assert (2, {'mock': 'result', 'mock': 'result'}) in matches
