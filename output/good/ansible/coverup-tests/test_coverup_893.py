# file lib/ansible/galaxy/api.py:293-296
# lines [293, 296]
# branches []

import pytest
from ansible.galaxy.api import GalaxyAPI
from ansible.module_utils._text import to_text

@pytest.fixture
def galaxy_api_instance(mocker):
    mocker.patch.object(GalaxyAPI, '__init__', return_value=None)
    galaxy_api_instance = GalaxyAPI()
    galaxy_api_instance.name = "TestAPI"
    return galaxy_api_instance

def test_galaxy_api_unicode(galaxy_api_instance):
    assert isinstance(galaxy_api_instance.__unicode__(), str)
    assert galaxy_api_instance.__unicode__() == to_text("TestAPI")
