# file: lib/ansible/galaxy/api.py:298-307
# asked: {"lines": [298, 301, 302, 303, 304, 305], "branches": []}
# gained: {"lines": [298, 301, 302, 303, 304, 305], "branches": []}

import pytest
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def galaxy_api():
    return GalaxyAPI(
        galaxy="test_galaxy",
        name="test_name",
        url="http://test_url",
        username="test_user",
        password="test_pass",
        token="test_token",
        validate_certs=True,
        available_api_versions={"v1": "1.0"},
        clear_response_cache=False,
        no_cache=True,
        priority=1
    )

def test_repr(galaxy_api):
    expected_repr = '<{instance!s} "test_name" @ http://test_url with priority 1>'.format(instance=galaxy_api)
    assert repr(galaxy_api) == expected_repr
