# file sanic/blueprint_group.py:59-71
# lines [59, 68, 69, 70, 71]
# branches []

import pytest
from sanic.blueprint_group import BlueprintGroup
from sanic.blueprints import Blueprint

@pytest.fixture
def blueprint_group():
    return BlueprintGroup(url_prefix='/group', version=1, strict_slashes=True)

@pytest.fixture
def blueprint():
    return Blueprint('test', url_prefix='/test')

def test_blueprint_group_initialization(blueprint_group):
    assert blueprint_group._url_prefix == '/group'
    assert blueprint_group._version == 1
    assert blueprint_group._strict_slashes is True

def test_blueprint_group_append(blueprint_group, blueprint):
    blueprint_group.append(blueprint)
    assert blueprint in blueprint_group._blueprints
    assert blueprint.url_prefix == '/group/test'
    assert blueprint.version == 1
    assert blueprint.strict_slashes is True

def test_blueprint_group_insert(blueprint_group, blueprint):
    blueprint_group.insert(0, blueprint)
    assert blueprint_group._blueprints[0] == blueprint
    assert blueprint.url_prefix == '/group/test'
    assert blueprint.version == 1
    assert blueprint.strict_slashes is True

def test_blueprint_group_extend(blueprint_group, blueprint):
    blueprint_group.extend([blueprint])
    assert blueprint in blueprint_group._blueprints
    assert blueprint.url_prefix == '/group/test'
    assert blueprint.version == 1
    assert blueprint.strict_slashes is True

def test_blueprint_group_remove(blueprint_group, blueprint):
    blueprint_group.append(blueprint)
    blueprint_group.remove(blueprint)
    assert blueprint not in blueprint_group._blueprints

def test_blueprint_group_delitem(blueprint_group, blueprint):
    blueprint_group.append(blueprint)
    del blueprint_group[0]
    assert blueprint not in blueprint_group._blueprints

def test_blueprint_group_getitem(blueprint_group, blueprint):
    blueprint_group.append(blueprint)
    assert blueprint_group[0] == blueprint

def test_blueprint_group_setitem(blueprint_group, blueprint):
    blueprint_group.append(blueprint)
    new_blueprint = Blueprint('new_test', url_prefix='/new_test')
    blueprint_group[0] = new_blueprint
    assert blueprint_group[0] == new_blueprint
    # The url_prefix of the new_blueprint should not be modified by the group
    assert new_blueprint.url_prefix == '/new_test'

def test_blueprint_group_len(blueprint_group, blueprint):
    blueprint_group.append(blueprint)
    assert len(blueprint_group) == 1

def test_blueprint_group_iter(blueprint_group, blueprint):
    blueprint_group.append(blueprint)
    assert list(iter(blueprint_group)) == [blueprint]

def test_blueprint_group_reversed(blueprint_group, blueprint):
    blueprint_group.append(blueprint)
    assert list(reversed(blueprint_group)) == [blueprint]

def test_blueprint_group_contains(blueprint_group, blueprint):
    blueprint_group.append(blueprint)
    assert blueprint in blueprint_group

def test_blueprint_group_index(blueprint_group, blueprint):
    blueprint_group.append(blueprint)
    assert blueprint_group.index(blueprint) == 0

def test_blueprint_group_count(blueprint_group, blueprint):
    blueprint_group.append(blueprint)
    assert blueprint_group.count(blueprint) == 1

def test_blueprint_group_pop(blueprint_group, blueprint):
    blueprint_group.append(blueprint)
    popped_blueprint = blueprint_group.pop()
    assert popped_blueprint == blueprint
    assert blueprint not in blueprint_group._blueprints
