# file: lib/ansible/galaxy/api.py:298-307
# asked: {"lines": [298, 301, 302, 303, 304, 305], "branches": []}
# gained: {"lines": [298, 301, 302, 303, 304, 305], "branches": []}

import pytest
from unittest.mock import Mock

# Assuming the GalaxyAPI class is defined in ansible/galaxy/api.py
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def galaxy_api_instance():
    galaxy = Mock()
    name = "TestAPI"
    url = "http://testserver.com"
    instance = GalaxyAPI(galaxy, name, url)
    instance._priority = 10
    return instance

def test_galaxy_api_repr(galaxy_api_instance):
    expected_repr = '<{instance!s} "{name!s}" @ {url!s} with priority {priority!s}>'.format(
        instance=galaxy_api_instance, name="TestAPI", url="http://testserver.com", priority=10
    )
    assert repr(galaxy_api_instance) == expected_repr
