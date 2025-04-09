# file lib/ansible/playbook/block.py:224-243
# lines [230, 231, 232, 233, 235, 237, 238, 239, 240, 241, 243]
# branches ['231->232', '231->235', '232->231', '232->233', '237->238', '237->239', '239->240', '239->243']

import pytest
from unittest.mock import Mock

# Assuming the Block class and its dependencies are imported from ansible.playbook.block
from ansible.playbook.block import Block

@pytest.fixture
def block_instance():
    block = Block()
    block._valid_attrs = ['attr1', 'attr2', 'block', 'rescue', 'always']
    block.attr1 = 'value1'
    block.attr2 = 'value2'
    block._role = Mock()
    block._role.serialize.return_value = {'role_key': 'role_value'}
    block._parent = Mock()
    block._parent.copy.return_value.serialize.return_value = {'parent_key': 'parent_value'}
    block._parent.__class__.__name__ = 'ParentClass'
    block.get_dep_chain = Mock(return_value='dep_chain_value')
    return block

def test_block_serialize(block_instance):
    data = block_instance.serialize()
    
    assert data['attr1'] == 'value1'
    assert data['attr2'] == 'value2'
    assert 'block' not in data
    assert 'rescue' not in data
    assert 'always' not in data
    assert data['dep_chain'] == 'dep_chain_value'
    assert data['role'] == {'role_key': 'role_value'}
    assert data['parent'] == {'parent_key': 'parent_value'}
    assert data['parent_type'] == 'ParentClass'
