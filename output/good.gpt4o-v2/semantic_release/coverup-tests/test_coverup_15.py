# file: semantic_release/hvcs.py:96-104
# asked: {"lines": [96, 97, 102, 103, 104], "branches": []}
# gained: {"lines": [96, 97, 102, 103, 104], "branches": []}

import pytest
from semantic_release.hvcs import Github
from semantic_release.settings import config

def test_github_domain_with_hvcs_domain(monkeypatch):
    monkeypatch.setattr(config, 'get', lambda key: 'custom.domain' if key == 'hvcs_domain' else None)
    assert Github.domain() == 'custom.domain'

def test_github_domain_without_hvcs_domain(monkeypatch):
    monkeypatch.setattr(config, 'get', lambda key: None)
    assert Github.domain() == Github.DEFAULT_DOMAIN
