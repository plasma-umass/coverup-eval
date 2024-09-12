# file: src/blib2to3/pytree.py:582-590
# asked: {"lines": [588, 589, 590], "branches": [[589, 0], [589, 590]]}
# gained: {"lines": [588, 589, 590], "branches": [[589, 590]]}

import pytest
from unittest.mock import MagicMock
from typing import List, Iterator, Tuple

# Assuming NL and _Results are defined somewhere in the module
NL = MagicMock()
_Results = dict

from blib2to3.pytree import BasePattern

class ConcretePattern(BasePattern):
    def match(self, node: NL, results: _Results = None) -> bool:
        return super().match(node, results)

class TestBasePattern:
    def test_generate_matches(self):
        # Create a mock for the match method
        pattern = ConcretePattern()
        pattern.match = MagicMock(return_value=True)
        
        # Create a list with one mock node
        nodes: List[NL] = [NL()]
        
        # Call generate_matches and collect the results
        matches = list(pattern.generate_matches(nodes))
        
        # Assert that the match method was called with the first node and an empty dict
        pattern.match.assert_called_once_with(nodes[0], {})
        
        # Assert that the result is as expected
        assert matches == [(1, {})]
