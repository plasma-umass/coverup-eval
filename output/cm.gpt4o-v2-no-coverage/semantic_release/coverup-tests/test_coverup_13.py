# file: semantic_release/hvcs.py:96-104
# asked: {"lines": [96, 97, 102, 103, 104], "branches": []}
# gained: {"lines": [96, 97, 102, 103, 104], "branches": []}

import pytest
from semantic_release.hvcs import Github
from semantic_release.settings import config

@pytest.fixture
def mock_config_get(mocker):
    return mocker.patch('semantic_release.settings.config.get')

def test_github_domain_with_custom_domain(mock_config_get):
    mock_config_get.return_value = 'custom.domain'
    assert Github.domain() == 'custom.domain'

def test_github_domain_with_default_domain(mock_config_get, monkeypatch):
    mock_config_get.return_value = None
    monkeypatch.setattr(Github, 'DEFAULT_DOMAIN', 'default.domain')
    assert Github.domain() == 'default.domain'
