# file: semantic_release/hvcs.py:502-508
# asked: {"lines": [502, 508], "branches": []}
# gained: {"lines": [502, 508], "branches": []}

import pytest
from unittest.mock import patch
from semantic_release.hvcs import check_token, get_hvcs

@pytest.fixture
def mock_get_hvcs(mocker):
    mock_hvcs = mocker.patch('semantic_release.hvcs.get_hvcs')
    return mock_hvcs

def test_check_token_exists(mock_get_hvcs):
    mock_get_hvcs.return_value.token.return_value = 'fake_token'
    assert check_token() is True

def test_check_token_not_exists(mock_get_hvcs):
    mock_get_hvcs.return_value.token.return_value = None
    assert check_token() is False
