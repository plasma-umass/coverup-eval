# file: semantic_release/hvcs.py:502-508
# asked: {"lines": [502, 508], "branches": []}
# gained: {"lines": [502, 508], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from semantic_release.hvcs import check_token, get_hvcs
from semantic_release.errors import ImproperConfigurationError

@pytest.fixture
def mock_get_hvcs():
    with patch('semantic_release.hvcs.get_hvcs') as mock:
        yield mock

def test_check_token_exists(mock_get_hvcs):
    mock_hvcs_instance = MagicMock()
    mock_hvcs_instance.token.return_value = "dummy_token"
    mock_get_hvcs.return_value = mock_hvcs_instance

    assert check_token() is True

def test_check_token_not_exists(mock_get_hvcs):
    mock_hvcs_instance = MagicMock()
    mock_hvcs_instance.token.return_value = None
    mock_get_hvcs.return_value = mock_hvcs_instance

    assert check_token() is False

def test_check_token_improper_configuration(mock_get_hvcs):
    mock_get_hvcs.side_effect = ImproperConfigurationError

    with pytest.raises(ImproperConfigurationError):
        check_token()
