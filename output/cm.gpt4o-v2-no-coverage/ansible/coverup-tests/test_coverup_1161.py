# file: lib/ansible/galaxy/api.py:309-318
# asked: {"lines": [312, 313, 315, 316, 317], "branches": [[312, 313], [312, 315]]}
# gained: {"lines": [312, 313, 315, 316, 317], "branches": [[312, 313], [312, 315]]}

import pytest
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def galaxy_api_instance():
    return GalaxyAPI(galaxy="test_galaxy", name="test_name", url="http://test_url", priority=1)

@pytest.fixture
def other_galaxy_api_instance():
    return GalaxyAPI(galaxy="test_galaxy", name="other_name", url="http://test_url", priority=2)

def test_lt_same_class(galaxy_api_instance, other_galaxy_api_instance):
    assert (galaxy_api_instance < other_galaxy_api_instance) == (galaxy_api_instance._priority > other_galaxy_api_instance._priority or galaxy_api_instance.name < other_galaxy_api_instance.name)

def test_lt_different_class(galaxy_api_instance):
    class OtherClass:
        pass

    other_instance = OtherClass()
    assert galaxy_api_instance.__lt__(other_instance) == NotImplemented
