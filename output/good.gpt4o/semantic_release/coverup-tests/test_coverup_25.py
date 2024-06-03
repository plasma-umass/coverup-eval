# file semantic_release/hvcs.py:493-499
# lines [493, 499]
# branches []

import pytest
from unittest.mock import patch
from semantic_release.hvcs import get_domain, get_hvcs

def test_get_domain(mocker):
    # Mock the get_hvcs function to return a mock object with a domain method
    mock_hvcs = mocker.Mock()
    mock_hvcs.domain.return_value = "example.com"
    mocker.patch('semantic_release.hvcs.get_hvcs', return_value=mock_hvcs)
    
    # Call the function and assert the expected result
    assert get_domain() == "example.com"
    
    # Verify that the domain method was called
    mock_hvcs.domain.assert_called_once()
