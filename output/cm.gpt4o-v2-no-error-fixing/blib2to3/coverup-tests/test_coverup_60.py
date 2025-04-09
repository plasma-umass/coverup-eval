# file: src/blib2to3/pytree.py:582-590
# asked: {"lines": [588, 589, 590], "branches": [[589, 0], [589, 590]]}
# gained: {"lines": [588, 589, 590], "branches": [[589, 0], [589, 590]]}

import pytest
from unittest.mock import MagicMock
from typing import List

# Assuming NL and _Results are defined somewhere in the module
NL = MagicMock()
_Results = dict

from blib2to3.pytree import BasePattern

class TestBasePattern:
    @pytest.fixture
    def base_pattern(self):
        # Create a mock subclass of BasePattern since BasePattern cannot be instantiated
        class MockPattern(BasePattern):
            def match(self, node: NL, results: _Results = None) -> bool:
                return True

        return MockPattern()

    def test_generate_matches(self, base_pattern):
        nodes = [NL()]
        matches = list(base_pattern.generate_matches(nodes))
        
        assert len(matches) == 1
        assert matches[0][0] == 1
        assert isinstance(matches[0][1], dict)

    def test_generate_matches_no_nodes(self, base_pattern):
        nodes = []
        matches = list(base_pattern.generate_matches(nodes))
        
        assert len(matches) == 0

    def test_generate_matches_no_match(self, base_pattern, monkeypatch):
        def mock_match(node, results=None):
            return False

        monkeypatch.setattr(base_pattern, "match", mock_match)
        
        nodes = [NL()]
        matches = list(base_pattern.generate_matches(nodes))
        
        assert len(matches) == 0
