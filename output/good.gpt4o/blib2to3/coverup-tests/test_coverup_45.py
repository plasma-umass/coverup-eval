# file src/blib2to3/pytree.py:582-590
# lines [582, 588, 589, 590]
# branches ['589->exit', '589->590']

import pytest
from unittest.mock import Mock
from blib2to3.pytree import BasePattern

class ConcretePattern(BasePattern):
    def match(self, node, results):
        return True

class TestBasePattern:
    @pytest.fixture
    def base_pattern(self):
        return ConcretePattern()

    def test_generate_matches(self, base_pattern):
        # Mock the match method to return True
        base_pattern.match = Mock(return_value=True)
        
        # Create a mock node
        mock_node = Mock()
        
        # Call generate_matches with a list containing the mock node
        matches = list(base_pattern.generate_matches([mock_node]))
        
        # Assert that the match method was called with the mock node and an empty dictionary
        base_pattern.match.assert_called_once_with(mock_node, {})
        
        # Assert that the result is as expected
        assert len(matches) == 1
        assert matches[0] == (1, {})

    def test_generate_matches_no_nodes(self, base_pattern):
        # Call generate_matches with an empty list
        matches = list(base_pattern.generate_matches([]))
        
        # Assert that no matches are generated
        assert matches == []
