# file lib/ansible/galaxy/api.py:293-296
# lines [296]
# branches []

import pytest
from unittest import mock
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def galaxy_api_instance():
    instance = GalaxyAPI(galaxy="test_galaxy", name="TestAPI", url="http://testurl.com")
    return instance

def test_unicode_method(galaxy_api_instance):
    with mock.patch('ansible.galaxy.api.to_text', return_value="TestAPI") as mock_to_text:
        result = galaxy_api_instance.__unicode__()
        mock_to_text.assert_called_once_with("TestAPI")
        assert result == "TestAPI"
