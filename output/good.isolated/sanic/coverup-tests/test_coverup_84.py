# file sanic/blueprint_group.py:143-154
# lines [143, 154]
# branches []

import pytest
from sanic import Blueprint
from sanic.blueprint_group import BlueprintGroup

@pytest.fixture
def blueprint_group():
    group = BlueprintGroup()
    group.append(Blueprint('blueprint_1'))
    group.append(Blueprint('blueprint_2'))
    group.append(Blueprint('blueprint_3'))
    return group

def test_blueprint_group_delitem(blueprint_group):
    # Precondition: Ensure there are 3 items in the group
    assert len(blueprint_group) == 3

    # Delete the item at index 1
    del blueprint_group[1]

    # Postcondition: Ensure the item was deleted and only 2 remain
    assert len(blueprint_group) == 2
    assert all(bp.name != 'blueprint_2' for bp in blueprint_group)

    # Cleanup is not necessary as the blueprint_group fixture is function-scoped
    # and will not affect other tests.
