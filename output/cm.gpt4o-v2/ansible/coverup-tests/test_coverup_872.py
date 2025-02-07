# file: lib/ansible/galaxy/api.py:288-291
# asked: {"lines": [288, 291], "branches": []}
# gained: {"lines": [288, 291], "branches": []}

import pytest
from ansible.module_utils._text import to_native
from ansible.galaxy.api import GalaxyAPI

def test_galaxy_api_str():
    # Arrange
    galaxy_api_instance = GalaxyAPI(galaxy=None, name="TestAPI", url="http://example.com")

    # Act
    result = str(galaxy_api_instance)

    # Assert
    assert result == to_native("TestAPI")

@pytest.fixture
def galaxy_api_instance():
    return GalaxyAPI(galaxy=None, name="TestAPI", url="http://example.com")

def test_galaxy_api_str_with_fixture(galaxy_api_instance):
    # Act
    result = str(galaxy_api_instance)

    # Assert
    assert result == to_native("TestAPI")
