# file sanic/blueprint_group.py:116-128
# lines [116, 128]
# branches []

import pytest
from sanic.blueprint_group import BlueprintGroup
from sanic.blueprints import Blueprint

@pytest.fixture
def blueprint_group():
    bp1 = Blueprint('bp1')
    bp2 = Blueprint('bp2')
    bp3 = Blueprint('bp3')
    group = BlueprintGroup()
    group.append(bp1)
    group.append(bp2)
    group.append(bp3)
    return group

def test_blueprint_group_getitem(blueprint_group):
    # Test getting a single item
    assert blueprint_group[1].name == 'bp2'
    
    # Test getting a slice
    slice_result = blueprint_group[1:3]
    assert len(slice_result) == 2
    assert slice_result[0].name == 'bp2'
    assert slice_result[1].name == 'bp3'
    
    # Test negative indexing
    assert blueprint_group[-1].name == 'bp3'
    
    # Test getting a slice with negative index
    slice_negative_index = blueprint_group[-3:-1]
    assert len(slice_negative_index) == 2
    assert slice_negative_index[0].name == 'bp1'
    assert slice_negative_index[1].name == 'bp2'
    
    # Test getting a slice with step
    slice_with_step = blueprint_group[::2]
    assert len(slice_with_step) == 2
    assert slice_with_step[0].name == 'bp1'
    assert slice_with_step[1].name == 'bp3'
    
    # Test out of range index
    with pytest.raises(IndexError):
        _ = blueprint_group[10]
    
    # Test invalid index type
    with pytest.raises(TypeError):
        _ = blueprint_group['invalid']
