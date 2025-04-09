# file sanic/blueprint_group.py:182-189
# lines [182, 189]
# branches []

import pytest
from sanic import Blueprint, Sanic
from sanic.blueprint_group import BlueprintGroup

@pytest.fixture
def blueprint_group():
    return BlueprintGroup()

@pytest.fixture
def blueprint():
    return Blueprint('test_blueprint')

def test_blueprint_group_append(blueprint_group, blueprint):
    assert len(blueprint_group) == 0  # Precondition: blueprint group is empty

    blueprint_group.append(blueprint)

    assert len(blueprint_group) == 1  # Postcondition: blueprint group has one item
    assert blueprint_group[0] == blueprint  # Postcondition: the item is the blueprint we added

    # Clean up is not necessary as the blueprint_group is a fixture and will be
    # freshly created for each test function.
