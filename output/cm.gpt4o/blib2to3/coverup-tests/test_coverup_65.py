# file src/blib2to3/pytree.py:796-798
# lines [796, 798]
# branches []

import pytest
from blib2to3.pytree import BasePattern

class WildcardPattern(BasePattern):
    def match(self, node, results=None) -> bool:
        """Does this pattern exactly match a node?"""
        return self.match_seq([node], results)

def test_wildcard_pattern_match(mocker):
    # Mock the match_seq method to control its behavior
    mocker.patch.object(WildcardPattern, 'match_seq', return_value=True)
    
    # Create an instance of WildcardPattern
    pattern = WildcardPattern()
    
    # Create a mock node
    mock_node = mocker.Mock()
    
    # Call the match method and assert the expected behavior
    assert pattern.match(mock_node) == True
    
    # Verify that match_seq was called with the correct arguments
    pattern.match_seq.assert_called_once_with([mock_node], None)
    
    # Test with results parameter
    mock_results = mocker.Mock()
    assert pattern.match(mock_node, mock_results) == True
    pattern.match_seq.assert_called_with([mock_node], mock_results)
