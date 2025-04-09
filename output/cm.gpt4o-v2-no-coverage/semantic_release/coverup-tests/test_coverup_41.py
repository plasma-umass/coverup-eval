# file: semantic_release/hvcs.py:502-508
# asked: {"lines": [508], "branches": []}
# gained: {"lines": [508], "branches": []}

import pytest
from unittest.mock import patch

# Assuming the check_token function is in a module named hvcs
from semantic_release.hvcs import check_token, get_hvcs

@pytest.fixture
def mock_get_hvcs():
    with patch('semantic_release.hvcs.get_hvcs') as mock:
        yield mock

def test_check_token_exists(mock_get_hvcs):
    mock_hvcs_instance = mock_get_hvcs.return_value
    mock_hvcs_instance.token.return_value = 'dummy_token'
    
    assert check_token() is True

def test_check_token_not_exists(mock_get_hvcs):
    mock_hvcs_instance = mock_get_hvcs.return_value
    mock_hvcs_instance.token.return_value = None
    
    assert check_token() is False
