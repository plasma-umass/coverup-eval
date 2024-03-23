# file semantic_release/hvcs.py:96-104
# lines [96, 97, 102, 103, 104]
# branches []

import pytest
from unittest.mock import patch, MagicMock
from semantic_release.hvcs import Github

@pytest.fixture
def mock_config():
    with patch('semantic_release.hvcs.config') as mock_config:
        mock_config.get = MagicMock()
        yield mock_config

def test_github_domain_default(mock_config):
    mock_config.get.return_value = None
    assert Github.domain() == Github.DEFAULT_DOMAIN
    mock_config.get.assert_called_once_with("hvcs_domain")

def test_github_domain_custom(mock_config):
    custom_domain = "custom.example.com"
    mock_config.get.return_value = custom_domain
    assert Github.domain() == custom_domain
    mock_config.get.assert_called_with("hvcs_domain")
