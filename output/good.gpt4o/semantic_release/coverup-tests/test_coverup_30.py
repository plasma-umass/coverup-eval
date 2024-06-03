# file semantic_release/hvcs.py:502-508
# lines [502, 508]
# branches []

import pytest
from unittest.mock import patch
from semantic_release.hvcs import check_token, get_hvcs

def test_check_token_with_token(mocker):
    mock_hvcs = mocker.Mock()
    mock_hvcs.token.return_value = "dummy_token"
    mocker.patch('semantic_release.hvcs.get_hvcs', return_value=mock_hvcs)

    assert check_token() is True

def test_check_token_without_token(mocker):
    mock_hvcs = mocker.Mock()
    mock_hvcs.token.return_value = None
    mocker.patch('semantic_release.hvcs.get_hvcs', return_value=mock_hvcs)

    assert check_token() is False
