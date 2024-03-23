# file semantic_release/hvcs.py:348-355
# lines [348, 349, 354, 355]
# branches []

import os
from unittest.mock import patch
import pytest
from semantic_release.hvcs import Gitlab

@pytest.fixture
def clean_env():
    original_domain = os.environ.get("CI_SERVER_HOST")
    if "CI_SERVER_HOST" in os.environ:
        del os.environ["CI_SERVER_HOST"]
    yield
    if original_domain is not None:
        os.environ["CI_SERVER_HOST"] = original_domain

def test_gitlab_domain_default(clean_env):
    assert Gitlab.domain() == "gitlab.com"

def test_gitlab_domain_from_env(clean_env):
    test_domain = "custom.gitlab.instance"
    with patch.dict(os.environ, {"CI_SERVER_HOST": test_domain}):
        assert Gitlab.domain() == test_domain

def test_gitlab_domain_from_config(clean_env, mocker):
    test_domain = "config.gitlab.instance"
    mocker.patch('semantic_release.hvcs.config.get', return_value=test_domain)
    assert Gitlab.domain() == test_domain
