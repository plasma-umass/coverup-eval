# file sanic/blueprint_group.py:110-114
# lines [110, 114]
# branches []

import pytest
from sanic import Blueprint
from sanic.blueprint_group import BlueprintGroup

@pytest.fixture
def blueprint_group():
    return BlueprintGroup()

def test_blueprint_group_iter(blueprint_group):
    # Create a mock blueprint to the group to test iteration
    mock_blueprint = Blueprint('mock_blueprint')
    blueprint_group.append(mock_blueprint)

    # Test __iter__ by converting to list
    blueprint_list = list(blueprint_group)

    # Assert that the mock blueprint is in the list
    assert mock_blueprint in blueprint_list

    # Clean up by removing the mock blueprint
    blueprint_group.remove(mock_blueprint)

    # Assert that the blueprint group is empty after cleanup
    assert len(blueprint_group) == 0
