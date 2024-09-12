# file: semantic_release/hvcs.py:493-499
# asked: {"lines": [493, 499], "branches": []}
# gained: {"lines": [493, 499], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from semantic_release.hvcs import get_domain, get_hvcs
from semantic_release.errors import ImproperConfigurationError

@pytest.fixture
def mock_get_hvcs():
    with patch('semantic_release.hvcs.get_hvcs') as mock:
        yield mock

def test_get_domain_valid_hvcs(mock_get_hvcs):
    mock_hvcs_instance = MagicMock()
    mock_hvcs_instance.domain.return_value = 'example.com'
    mock_get_hvcs.return_value = mock_hvcs_instance

    domain = get_domain()
    assert domain == 'example.com'
    mock_get_hvcs.assert_called_once()
    mock_hvcs_instance.domain.assert_called_once()

def test_get_domain_invalid_hvcs(mock_get_hvcs):
    mock_get_hvcs.side_effect = ImproperConfigurationError('Invalid HVCS')

    with pytest.raises(ImproperConfigurationError, match='Invalid HVCS'):
        get_domain()
    mock_get_hvcs.assert_called_once()
