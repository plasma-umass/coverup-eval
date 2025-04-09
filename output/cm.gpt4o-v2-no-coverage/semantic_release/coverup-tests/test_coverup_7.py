# file: semantic_release/hvcs.py:106-116
# asked: {"lines": [106, 107, 114, 115, 116], "branches": []}
# gained: {"lines": [106, 107, 114, 115, 116], "branches": []}

import pytest
from semantic_release.hvcs import Github
from semantic_release.settings import config

@pytest.fixture
def reset_config():
    original_config = config.copy()
    yield
    config.clear()
    config.update(original_config)

def test_api_url_with_custom_domain(reset_config, monkeypatch):
    monkeypatch.setitem(config, 'hvcs_domain', 'custom.domain.com')
    assert Github.api_url() == 'https://custom.domain.com'

def test_api_url_with_default_domain(reset_config, monkeypatch):
    monkeypatch.delitem(config, 'hvcs_domain', raising=False)
    assert Github.api_url() == 'https://api.github.com'
