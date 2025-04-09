# file semantic_release/hvcs.py:96-104
# lines [96, 97, 102, 103, 104]
# branches []

import pytest
from unittest.mock import patch
from semantic_release.hvcs import Github, config

@pytest.fixture
def mock_config(mocker):
    return mocker.patch('semantic_release.hvcs.config')

def test_github_domain_default(mock_config):
    mock_config.get.return_value = None
    assert Github.domain() == Github.DEFAULT_DOMAIN

def test_github_domain_custom(mock_config):
    custom_domain = "custom.github.com"
    mock_config.get.return_value = custom_domain
    assert Github.domain() == custom_domain
