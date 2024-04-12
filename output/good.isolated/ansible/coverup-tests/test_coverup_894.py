# file lib/ansible/galaxy/api.py:288-291
# lines [288, 291]
# branches []

import pytest
from ansible.galaxy.api import GalaxyAPI
from ansible.module_utils._text import to_native

class MockGalaxyAPI(GalaxyAPI):
    def __init__(self, name):
        self.name = name

@pytest.fixture
def galaxy_api():
    return MockGalaxyAPI(name="test_galaxy_api")

def test_galaxy_api_str(galaxy_api):
    assert str(galaxy_api) == to_native("test_galaxy_api")
