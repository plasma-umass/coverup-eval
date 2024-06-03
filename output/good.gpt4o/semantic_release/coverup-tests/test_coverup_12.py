# file semantic_release/hvcs.py:357-363
# lines [357, 358, 363]
# branches []

import pytest
from unittest.mock import patch

# Assuming the Gitlab class is imported from semantic_release.hvcs
from semantic_release.hvcs import Gitlab

@pytest.fixture
def mock_gitlab_domain(mocker):
    mocker.patch.object(Gitlab, 'domain', return_value='gitlab.com')
    yield
    mocker.stopall()

def test_gitlab_api_url(mock_gitlab_domain):
    expected_url = "https://gitlab.com"
    assert Gitlab.api_url() == expected_url
