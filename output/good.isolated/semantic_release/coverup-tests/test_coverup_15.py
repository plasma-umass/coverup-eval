# file semantic_release/hvcs.py:357-363
# lines [357, 358, 363]
# branches []

import pytest
from semantic_release.hvcs import Gitlab

def test_gitlab_api_url(mocker):
    # Mock the domain method to return a specific domain
    mocker.patch.object(Gitlab, 'domain', return_value='gitlab.com')

    # Call the api_url method and assert the result
    expected_url = 'https://gitlab.com'
    assert Gitlab.api_url() == expected_url

    # Cleanup is handled by pytest-mock, which automatically undoes patches after each test
