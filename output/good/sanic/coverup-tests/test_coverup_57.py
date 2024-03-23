# file sanic/blueprint_group.py:191-200
# lines [191, 200]
# branches []

import pytest
from sanic import Blueprint, Sanic
from sanic.blueprint_group import BlueprintGroup

@pytest.fixture
def blueprint_group():
    return BlueprintGroup()

@pytest.fixture
def blueprint():
    return Blueprint("test_blueprint")

def test_blueprint_group_insert(blueprint_group, blueprint):
    # Precondition: blueprint group should be empty
    assert len(blueprint_group) == 0

    # Action: insert a blueprint at index 0
    blueprint_group.insert(0, blueprint)

    # Postcondition: blueprint group should have one item
    assert len(blueprint_group) == 1
    assert blueprint_group[0] == blueprint

    # Clean up: remove the inserted blueprint
    del blueprint_group[0]
    assert len(blueprint_group) == 0
