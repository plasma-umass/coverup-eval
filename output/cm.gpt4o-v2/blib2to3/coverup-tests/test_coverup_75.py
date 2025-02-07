# file: src/blib2to3/pytree.py:796-798
# asked: {"lines": [796, 798], "branches": []}
# gained: {"lines": [796, 798], "branches": []}

import pytest
from blib2to3.pytree import WildcardPattern

class MockNode:
    pass

def test_wildcardpattern_match(mocker):
    # Create a mock node
    node = MockNode()
    
    # Create a WildcardPattern instance with content to avoid UnboundLocalError
    pattern = WildcardPattern(content=[['a']])
    
    # Mock the match_seq method to return True
    mocker.patch.object(pattern, 'match_seq', return_value=True)
    
    # Call the match method and assert it returns True
    assert pattern.match(node) == True
    
    # Mock the match_seq method to return False
    mocker.patch.object(pattern, 'match_seq', return_value=False)
    
    # Call the match method and assert it returns False
    assert pattern.match(node) == False
