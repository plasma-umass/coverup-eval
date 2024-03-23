# file lib/ansible/galaxy/api.py:298-307
# lines [301, 302, 303, 304, 305]
# branches []

import pytest
from ansible.galaxy.api import GalaxyAPI

class TestGalaxyAPI:

    @pytest.fixture
    def galaxy_api_instance(self, mocker):
        mocker.patch.object(GalaxyAPI, '__init__', return_value=None)
        api_instance = GalaxyAPI()
        api_instance.name = "TestAPI"
        api_instance._priority = 10
        api_instance.api_server = "https://api.test.com"
        return api_instance

    def test_galaxy_api_repr(self, galaxy_api_instance):
        expected_repr = '<{instance!s} "TestAPI" @ https://api.test.com with priority 10>'.format(instance=galaxy_api_instance)
        assert repr(galaxy_api_instance) == expected_repr
