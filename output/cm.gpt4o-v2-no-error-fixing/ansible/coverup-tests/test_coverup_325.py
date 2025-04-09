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
    assert galaxy_api_instance.__lt__(other_galaxy_api_instance) is False

def test_lt_with_lower_priority(galaxy_api_instance, other_galaxy_api_instance):
    galaxy_api_instance._priority = 3
    assert galaxy_api_instance.__lt__(other_galaxy_api_instance) is True

def test_lt_with_equal_priority_and_name(galaxy_api_instance, other_galaxy_api_instance):
    other_galaxy_api_instance._priority = 1
    other_galaxy_api_instance.name = "test_name"
    assert galaxy_api_instance.__lt__(other_galaxy_api_instance) is False
