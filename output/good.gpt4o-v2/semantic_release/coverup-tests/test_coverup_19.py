# file: semantic_release/hvcs.py:348-355
# asked: {"lines": [348, 349, 354, 355], "branches": []}
# gained: {"lines": [348, 349, 354, 355], "branches": []}

import os
import pytest
from semantic_release.settings import config
from semantic_release.hvcs import Gitlab

def test_gitlab_domain_from_config(monkeypatch):
    monkeypatch.setattr(config, 'get', lambda key, default=None: 'custom.domain' if key == 'hvcs_domain' else default)
    assert Gitlab.domain() == 'custom.domain'

def test_gitlab_domain_from_env(monkeypatch):
    monkeypatch.setattr(config, 'get', lambda key, default=None: default)
    monkeypatch.setenv('CI_SERVER_HOST', 'env.domain')
    assert Gitlab.domain() == 'env.domain'

def test_gitlab_domain_default(monkeypatch):
    monkeypatch.setattr(config, 'get', lambda key, default=None: default)
    monkeypatch.delenv('CI_SERVER_HOST', raising=False)
    assert Gitlab.domain() == 'gitlab.com'
