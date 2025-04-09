# file: semantic_release/hvcs.py:96-104
# asked: {"lines": [102, 103, 104], "branches": []}
# gained: {"lines": [102, 103, 104], "branches": []}

import pytest
from semantic_release.hvcs import Github
from semantic_release.settings import config

@pytest.fixture
def reset_config():
    original_config = config.copy()
    yield
    config.clear()
    config.update(original_config)

def test_github_domain_with_hvcs_domain(monkeypatch, reset_config):
    monkeypatch.setitem(config, "hvcs_domain", "custom.domain.com")
    assert Github.domain() == "custom.domain.com"

def test_github_domain_without_hvcs_domain(reset_config):
    if "hvcs_domain" in config:
        del config["hvcs_domain"]
    assert Github.domain() == Github.DEFAULT_DOMAIN
