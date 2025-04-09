# file: src/blib2to3/pytree.py:796-798
# asked: {"lines": [796, 798], "branches": []}
# gained: {"lines": [796, 798], "branches": []}

import pytest
from blib2to3.pytree import WildcardPattern

class MockNode:
    pass

def test_wildcardpattern_match(mocker):
    mock_node = MockNode()
    mock_results = {}

    # Create an instance of WildcardPattern with valid parameters
    pattern = WildcardPattern(content=[['a']], min=0, max=2147483647)

    # Mock the match_seq method to control its behavior
    mock_match_seq = mocker.patch.object(pattern, 'match_seq', return_value=True)

    # Call the match method
    result = pattern.match(mock_node, mock_results)

    # Assertions
    mock_match_seq.assert_called_once_with([mock_node], mock_results)
    assert result is True

    # Clean up
    del pattern
    del mock_node
    del mock_results
