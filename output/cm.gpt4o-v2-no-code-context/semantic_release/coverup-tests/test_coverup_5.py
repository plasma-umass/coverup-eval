# file: semantic_release/hvcs.py:357-363
# asked: {"lines": [357, 358, 363], "branches": []}
# gained: {"lines": [357, 358, 363], "branches": []}

import pytest
from semantic_release.hvcs import Gitlab

def test_gitlab_api_url(monkeypatch):
    # Mock the domain method to return a specific domain
    monkeypatch.setattr(Gitlab, 'domain', lambda: 'gitlab.com')
    
    # Call the api_url method and assert the expected URL
    expected_url = "https://gitlab.com"
    assert Gitlab.api_url() == expected_url
