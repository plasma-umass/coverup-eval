# file: semantic_release/hvcs.py:106-116
# asked: {"lines": [106, 107, 114, 115, 116], "branches": []}
# gained: {"lines": [106, 107, 114, 115, 116], "branches": []}

import pytest
from semantic_release.hvcs import Github, config

@pytest.fixture
def reset_config():
    original_config = config.copy()
    yield
    config.clear()
    config.update(original_config)

def test_github_api_url_default_domain(reset_config, monkeypatch):
    monkeypatch.setattr(Github, 'DEFAULT_DOMAIN', 'github.com')
    config.pop("hvcs_domain", None)  # Ensure hvcs_domain is not set
    expected_url = "https://api.github.com"
    assert Github.api_url() == expected_url

def test_github_api_url_custom_domain(reset_config):
    custom_domain = "custom.github.com"
    config["hvcs_domain"] = custom_domain
    expected_url = f"https://{custom_domain}"
    assert Github.api_url() == expected_url
