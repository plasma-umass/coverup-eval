# file: lib/ansible/playbook/block.py:224-243
# asked: {"lines": [224, 230, 231, 232, 233, 235, 237, 238, 239, 240, 241, 243], "branches": [[231, 232], [231, 235], [232, 231], [232, 233], [237, 238], [237, 239], [239, 240], [239, 243]]}
# gained: {"lines": [224, 230, 231, 232, 233, 235, 237, 238, 239, 240, 241, 243], "branches": [[231, 232], [231, 235], [232, 231], [232, 233], [237, 238], [237, 239], [239, 240], [239, 243]]}

import pytest
from unittest.mock import Mock
from ansible.playbook.block import Block

@pytest.fixture
def block_instance():
    return Block()

def test_serialize_no_role_no_parent(block_instance):
    block_instance._valid_attrs = ['attr1', 'attr2', 'block', 'rescue', 'always']
    block_instance.attr1 = 'value1'
    block_instance.attr2 = 'value2'
    block_instance._role = None
    block_instance._parent = None
    block_instance.get_dep_chain = Mock(return_value='dep_chain_value')

    serialized_data = block_instance.serialize()

    assert serialized_data == {
        'attr1': 'value1',
        'attr2': 'value2',
        'dep_chain': 'dep_chain_value'
    }

def test_serialize_with_role(block_instance):
    block_instance._valid_attrs = ['attr1', 'attr2', 'block', 'rescue', 'always']
    block_instance.attr1 = 'value1'
    block_instance.attr2 = 'value2'
    block_instance._role = Mock()
    block_instance._role.serialize = Mock(return_value='role_serialized')
    block_instance._parent = None
    block_instance.get_dep_chain = Mock(return_value='dep_chain_value')

    serialized_data = block_instance.serialize()

    assert serialized_data == {
        'attr1': 'value1',
        'attr2': 'value2',
        'dep_chain': 'dep_chain_value',
        'role': 'role_serialized'
    }

def test_serialize_with_parent(block_instance):
    block_instance._valid_attrs = ['attr1', 'attr2', 'block', 'rescue', 'always']
    block_instance.attr1 = 'value1'
    block_instance.attr2 = 'value2'
    block_instance._role = None
    block_instance._parent = Mock()
    block_instance._parent.copy = Mock(return_value=block_instance._parent)
    block_instance._parent.serialize = Mock(return_value='parent_serialized')
    block_instance._parent.__class__.__name__ = 'ParentClass'
    block_instance.get_dep_chain = Mock(return_value='dep_chain_value')

    serialized_data = block_instance.serialize()

    assert serialized_data == {
        'attr1': 'value1',
        'attr2': 'value2',
        'dep_chain': 'dep_chain_value',
        'parent': 'parent_serialized',
        'parent_type': 'ParentClass'
    }
