# file: lib/ansible/galaxy/api.py:309-318
# asked: {"lines": [309, 312, 313, 315, 316, 317], "branches": [[312, 313], [312, 315]]}
# gained: {"lines": [309, 312, 313, 315, 316, 317], "branches": [[312, 313], [312, 315]]}

import pytest
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def galaxy_api_instance():
    return GalaxyAPI(galaxy="test_galaxy", name="test_name", url="http://test_url", priority=1)

@pytest.fixture
def other_galaxy_api_instance():
    return GalaxyAPI(galaxy="test_galaxy", name="other_name", url="http://test_url", priority=2)

def test_lt_with_non_galaxy_api_instance(galaxy_api_instance):
    assert galaxy_api_instance.__lt__(object()) == NotImplemented

def test_lt_with_higher_priority(galaxy_api_instance, other_galaxy_api_instance):
    assert (other_galaxy_api_instance < galaxy_api_instance) == True

def test_lt_with_same_priority_and_name(galaxy_api_instance):
    same_priority_instance = GalaxyAPI(galaxy="test_galaxy", name="test_name", url="http://test_url", priority=1)
    assert (galaxy_api_instance < same_priority_instance) == False
