# file: semantic_release/hvcs.py:357-363
# asked: {"lines": [357, 358, 363], "branches": []}
# gained: {"lines": [357, 358, 363], "branches": []}

import pytest
from semantic_release.hvcs import Gitlab

def test_gitlab_api_url(monkeypatch):
    # Mock the domain method to return a known value
    monkeypatch.setattr(Gitlab, "domain", lambda: "gitlab.com")
    
    # Call the api_url method and check the result
    result = Gitlab.api_url()
    assert result == "https://gitlab.com"
