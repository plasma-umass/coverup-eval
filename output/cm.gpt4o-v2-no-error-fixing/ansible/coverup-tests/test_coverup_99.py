# file: lib/ansible/playbook/block.py:224-243
# asked: {"lines": [224, 230, 231, 232, 233, 235, 237, 238, 239, 240, 241, 243], "branches": [[231, 232], [231, 235], [232, 231], [232, 233], [237, 238], [237, 239], [239, 240], [239, 243]]}
# gained: {"lines": [224, 230, 231, 232, 233, 235, 237, 238, 239, 240, 241, 243], "branches": [[231, 232], [231, 235], [232, 231], [232, 233], [237, 238], [237, 239], [239, 240], [239, 243]]}

import pytest
from ansible.playbook.block import Block
from unittest.mock import Mock

@pytest.fixture
def block_instance():
    parent_block = Mock()
    parent_block.copy.return_value.serialize.return_value = {'mock': 'parent'}
    parent_block.__class__.__name__ = 'MockParent'
    
    role = Mock()
    role.serialize.return_value = {'mock': 'role'}
    
    block = Block(parent_block=parent_block, role=role)
    block._valid_attrs = ['attr1', 'attr2', 'block', 'rescue', 'always']
    block.attr1 = 'value1'
    block.attr2 = 'value2'
    block._dep_chain = 'dep_chain_value'
    
    return block

def test_serialize_with_role_and_parent(block_instance):
    serialized_data = block_instance.serialize()
    
    assert serialized_data['attr1'] == 'value1'
    assert serialized_data['attr2'] == 'value2'
    assert serialized_data['dep_chain'] == 'dep_chain_value'
    assert serialized_data['role'] == {'mock': 'role'}
    assert serialized_data['parent'] == {'mock': 'parent'}
    assert serialized_data['parent_type'] == 'MockParent'

def test_serialize_without_role(block_instance):
    block_instance._role = None
    serialized_data = block_instance.serialize()
    
    assert 'role' not in serialized_data

def test_serialize_without_parent(block_instance):
    block_instance._parent = None
    serialized_data = block_instance.serialize()
    
    assert 'parent' not in serialized_data
    assert 'parent_type' not in serialized_data
