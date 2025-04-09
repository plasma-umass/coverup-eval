# file: semantic_release/hvcs.py:357-363
# asked: {"lines": [357, 358, 363], "branches": []}
# gained: {"lines": [357, 358, 363], "branches": []}

import os
import pytest
from semantic_release.hvcs import Gitlab
from semantic_release.settings import config

@pytest.fixture
def clear_env_and_config(monkeypatch):
    # Clear environment variables and config before each test
    monkeypatch.delenv('CI_SERVER_HOST', raising=False)
    config.clear()
    yield
    # Clear environment variables and config after each test
    monkeypatch.delenv('CI_SERVER_HOST', raising=False)
    config.clear()

def test_api_url_with_config_domain(monkeypatch, clear_env_and_config):
    # Set the config domain
    config['hvcs_domain'] = 'custom.gitlab.com'
    assert Gitlab.api_url() == 'https://custom.gitlab.com'

def test_api_url_with_env_domain(monkeypatch, clear_env_and_config):
    # Set the environment variable
    monkeypatch.setenv('CI_SERVER_HOST', 'env.gitlab.com')
    assert Gitlab.api_url() == 'https://env.gitlab.com'

def test_api_url_with_default_domain(clear_env_and_config):
    # No config or environment variable set
    assert Gitlab.api_url() == 'https://gitlab.com'
