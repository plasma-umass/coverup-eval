# file sanic/blueprint_group.py:82-89
# lines [82, 83, 89]
# branches []

import pytest
from sanic import Blueprint, Sanic
from sanic.blueprint_group import BlueprintGroup

@pytest.fixture
def blueprint_group():
    group = BlueprintGroup()
    yield group
    group.clear()

def test_blueprint_group_blueprints_property(blueprint_group):
    bp1 = Blueprint('bp1')
    bp2 = Blueprint('bp2')
    blueprint_group.append(bp1)
    blueprint_group.append(bp2)

    blueprints = blueprint_group.blueprints

    assert isinstance(blueprints, list)
    assert bp1 in blueprints
    assert bp2 in blueprints
    assert len(blueprints) == 2

    blueprint_group.pop()
    blueprints_after_pop = blueprint_group.blueprints

    assert bp1 in blueprints_after_pop
    assert bp2 not in blueprints_after_pop
    assert len(blueprints_after_pop) == 1
