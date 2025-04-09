# file: src/blib2to3/pytree.py:951-978
# asked: {"lines": [951, 966, 967, 969, 970, 971, 972, 974, 975, 976, 977, 978], "branches": [[966, 967], [966, 969], [970, 0], [970, 971], [971, 972], [971, 974], [974, 970], [974, 975]]}
# gained: {"lines": [951, 966, 967, 969, 970, 971, 972, 974, 975, 976, 977, 978], "branches": [[966, 967], [966, 969], [970, 0], [970, 971], [971, 972], [971, 974], [974, 970], [974, 975]]}

import pytest
from unittest.mock import Mock
from typing import List, Iterator, Tuple, Dict

# Assuming BasePattern and NL are defined somewhere in the module
class BasePattern:
    def generate_matches(self, nodes: List['NL']) -> Iterator[Tuple[int, Dict]]:
        pass

class NL:
    pass

# Import the function to be tested
from blib2to3.pytree import generate_matches

def test_generate_matches_no_patterns():
    patterns = []
    nodes = [Mock(spec=NL)]
    matches = list(generate_matches(patterns, nodes))
    assert matches == [(0, {})]

def test_generate_matches_single_pattern_no_rest():
    pattern = Mock(spec=BasePattern)
    pattern.generate_matches.return_value = iter([(1, {'a': 1})])
    patterns = [pattern]
    nodes = [Mock(spec=NL)]
    
    matches = list(generate_matches(patterns, nodes))
    
    assert matches == [(1, {'a': 1})]
    pattern.generate_matches.assert_called_once_with(nodes)

def test_generate_matches_single_pattern_with_rest():
    pattern1 = Mock(spec=BasePattern)
    pattern1.generate_matches.return_value = iter([(1, {'a': 1})])
    pattern2 = Mock(spec=BasePattern)
    pattern2.generate_matches.return_value = iter([(1, {'b': 2})])
    
    patterns = [pattern1, pattern2]
    nodes = [Mock(spec=NL), Mock(spec=NL)]
    
    matches = list(generate_matches(patterns, nodes))
    
    assert matches == [(2, {'a': 1, 'b': 2})]
    pattern1.generate_matches.assert_called_once_with(nodes)
    pattern2.generate_matches.assert_called_once_with(nodes[1:])

def test_generate_matches_multiple_patterns():
    pattern1 = Mock(spec=BasePattern)
    pattern1.generate_matches.return_value = iter([(1, {'a': 1})])
    pattern2 = Mock(spec=BasePattern)
    pattern2.generate_matches.return_value = iter([(1, {'b': 2})])
    pattern3 = Mock(spec=BasePattern)
    pattern3.generate_matches.return_value = iter([(1, {'c': 3})])
    
    patterns = [pattern1, pattern2, pattern3]
    nodes = [Mock(spec=NL), Mock(spec=NL), Mock(spec=NL)]
    
    matches = list(generate_matches(patterns, nodes))
    
    assert matches == [(3, {'a': 1, 'b': 2, 'c': 3})]
    pattern1.generate_matches.assert_called_once_with(nodes)
    pattern2.generate_matches.assert_called_once_with(nodes[1:])
    pattern3.generate_matches.assert_called_once_with(nodes[2:])
