# file semantic_release/hvcs.py:106-116
# lines [106, 107, 114, 115, 116]
# branches []

import pytest
from unittest.mock import patch
from semantic_release.hvcs import Github

@pytest.fixture
def mock_config(mocker):
    return mocker.patch('semantic_release.hvcs.config.get')

def test_github_api_url_default_domain(mock_config):
    mock_config.return_value = None
    expected_url = "https://api.github.com"
    assert Github.api_url() == expected_url

def test_github_api_url_custom_domain(mock_config):
    custom_domain = "custom.domain.com"
    mock_config.return_value = custom_domain
    expected_url = f"https://{custom_domain}"
    assert Github.api_url() == expected_url
