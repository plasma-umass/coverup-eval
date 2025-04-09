# file sanic/blueprint_group.py:101-108
# lines [101, 102, 108]
# branches []

import pytest
from sanic.blueprint_group import BlueprintGroup

@pytest.fixture
def blueprint_group():
    return BlueprintGroup()

def test_strict_slashes_property(blueprint_group):
    # Initially, strict_slashes should be None
    assert blueprint_group.strict_slashes is None

    # Set strict_slashes to True
    blueprint_group._strict_slashes = True
    assert blueprint_group.strict_slashes is True

    # Set strict_slashes to False
    blueprint_group._strict_slashes = False
    assert blueprint_group.strict_slashes is False

    # Clean up by setting strict_slashes back to None
    blueprint_group._strict_slashes = None
    assert blueprint_group.strict_slashes is None
