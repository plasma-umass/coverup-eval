# file: semantic_release/hvcs.py:106-116
# asked: {"lines": [106, 107, 114, 115, 116], "branches": []}
# gained: {"lines": [106, 107, 114, 115, 116], "branches": []}

import pytest
from semantic_release.hvcs import Github
from semantic_release.settings import config

def test_github_api_url_with_custom_domain(monkeypatch):
    monkeypatch.setattr(config, "get", lambda key: "custom.domain" if key == "hvcs_domain" else None)
    assert Github.api_url() == "https://custom.domain"

def test_github_api_url_with_default_domain(monkeypatch):
    monkeypatch.setattr(config, "get", lambda key: None)
    assert Github.api_url() == "https://api.github.com"
