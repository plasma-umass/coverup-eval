# file sanic/blueprint_group.py:156-162
# lines [156, 162]
# branches []

import pytest
from sanic.blueprint_group import BlueprintGroup
from sanic.blueprints import Blueprint

@pytest.fixture
def blueprint_group():
    group = BlueprintGroup()
    yield group
    group.clear()

def test_blueprint_group_len(blueprint_group):
    assert len(blueprint_group) == 0, "Length of empty BlueprintGroup should be 0"
    
    bp1 = Blueprint('bp1')
    blueprint_group.append(bp1)
    assert len(blueprint_group) == 1, "Length of BlueprintGroup should be 1 after adding a blueprint"
    
    bp2 = Blueprint('bp2')
    blueprint_group.append(bp2)
    assert len(blueprint_group) == 2, "Length of BlueprintGroup should be 2 after adding another blueprint"
    
    blueprint_group.pop()
    assert len(blueprint_group) == 1, "Length of BlueprintGroup should be 1 after removing a blueprint"
    
    blueprint_group.pop()
    assert len(blueprint_group) == 0, "Length of BlueprintGroup should be 0 after removing all blueprints"
