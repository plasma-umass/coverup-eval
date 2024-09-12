# file: semantic_release/hvcs.py:357-363
# asked: {"lines": [357, 358, 363], "branches": []}
# gained: {"lines": [357, 358, 363], "branches": []}

import pytest
from semantic_release.hvcs import Gitlab

@pytest.fixture
def mock_gitlab_domain(monkeypatch):
    def mock_domain():
        return "gitlab.com"
    monkeypatch.setattr(Gitlab, "domain", mock_domain)

def test_gitlab_api_url(mock_gitlab_domain):
    expected_url = "https://gitlab.com"
    assert Gitlab.api_url() == expected_url
