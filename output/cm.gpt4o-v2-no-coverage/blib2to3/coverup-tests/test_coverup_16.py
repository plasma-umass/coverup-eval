# file: src/blib2to3/pytree.py:951-978
# asked: {"lines": [951, 966, 967, 969, 970, 971, 972, 974, 975, 976, 977, 978], "branches": [[966, 967], [966, 969], [970, 0], [970, 971], [971, 972], [971, 974], [974, 970], [974, 975]]}
# gained: {"lines": [951, 966, 967, 969, 970, 971, 972, 974, 975, 976, 977, 978], "branches": [[966, 967], [966, 969], [970, 0], [970, 971], [971, 972], [971, 974], [974, 970], [974, 975]]}

import pytest
from unittest.mock import MagicMock
from typing import List, Tuple, Iterator, Union

# Assuming BasePattern, Node, and Leaf are defined in the module blib2to3.pytree
from blib2to3.pytree import generate_matches, BasePattern

NL = Union['Node', 'Leaf']

class TestGenerateMatches:
    @pytest.fixture
    def mock_pattern(self, monkeypatch):
        mock = MagicMock(spec=BasePattern)
        monkeypatch.setattr('blib2to3.pytree.BasePattern', mock)
        return mock

    def test_generate_matches_no_patterns(self):
        patterns = []
        nodes = [MagicMock()]
        result = list(generate_matches(patterns, nodes))
        assert result == [(0, {})]

    def test_generate_matches_single_pattern(self, mock_pattern):
        pattern_instance = mock_pattern.return_value
        pattern_instance.generate_matches.return_value = iter([(1, {'a': 1})])
        
        patterns = [pattern_instance]
        nodes = [MagicMock()]
        
        result = list(generate_matches(patterns, nodes))
        assert result == [(1, {'a': 1})]
        pattern_instance.generate_matches.assert_called_once_with(nodes)

    def test_generate_matches_multiple_patterns(self, mock_pattern):
        pattern_instance_1 = MagicMock(spec=BasePattern)
        pattern_instance_2 = MagicMock(spec=BasePattern)
        
        pattern_instance_1.generate_matches.return_value = iter([(1, {'a': 1})])
        pattern_instance_2.generate_matches.return_value = iter([(1, {'b': 2})])
        
        patterns = [pattern_instance_1, pattern_instance_2]
        nodes = [MagicMock(), MagicMock()]
        
        result = list(generate_matches(patterns, nodes))
        assert result == [(2, {'a': 1, 'b': 2})]
        pattern_instance_1.generate_matches.assert_called_once_with(nodes)
        pattern_instance_2.generate_matches.assert_called_once_with(nodes[1:])

    def test_generate_matches_no_match_in_first_pattern(self, mock_pattern):
        pattern_instance_1 = MagicMock(spec=BasePattern)
        pattern_instance_2 = MagicMock(spec=BasePattern)
        
        pattern_instance_1.generate_matches.return_value = iter([])
        pattern_instance_2.generate_matches.return_value = iter([(1, {'b': 2})])
        
        patterns = [pattern_instance_1, pattern_instance_2]
        nodes = [MagicMock(), MagicMock()]
        
        result = list(generate_matches(patterns, nodes))
        assert result == []
        pattern_instance_1.generate_matches.assert_called_once_with(nodes)
        pattern_instance_2.generate_matches.assert_not_called()
