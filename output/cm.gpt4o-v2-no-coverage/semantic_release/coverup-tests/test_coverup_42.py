# file: semantic_release/hvcs.py:493-499
# asked: {"lines": [499], "branches": []}
# gained: {"lines": [499], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from semantic_release.hvcs import get_domain, get_hvcs
from semantic_release.errors import ImproperConfigurationError

@pytest.fixture
def mock_config():
    with patch('semantic_release.hvcs.config') as mock_config:
        yield mock_config

@pytest.fixture
def mock_globals():
    with patch('semantic_release.hvcs.globals') as mock_globals:
        yield mock_globals

def test_get_domain_valid_hvcs(mock_config, mock_globals):
    mock_config.get.return_value = 'Base'
    mock_hvcs_instance = MagicMock()
    mock_hvcs_instance.domain.return_value = 'example.com'
    mock_globals.return_value = {'Base': mock_hvcs_instance}

    domain = get_domain()

    assert domain == 'example.com'
    mock_hvcs_instance.domain.assert_called_once()

def test_get_domain_invalid_hvcs(mock_config, mock_globals):
    mock_config.get.return_value = 'InvalidHVCS'
    mock_globals.return_value = {}

    with pytest.raises(ImproperConfigurationError):
        get_domain()
