# file: lib/ansible/playbook/block.py:224-243
# asked: {"lines": [224, 230, 231, 232, 233, 235, 237, 238, 239, 240, 241, 243], "branches": [[231, 232], [231, 235], [232, 231], [232, 233], [237, 238], [237, 239], [239, 240], [239, 243]]}
# gained: {"lines": [224, 230, 231, 232, 233, 235, 237, 238, 239, 240, 241, 243], "branches": [[231, 232], [231, 235], [232, 231], [232, 233], [237, 238], [237, 239], [239, 240], [239, 243]]}

import pytest
from unittest.mock import Mock

# Assuming Block and its dependencies are imported from ansible.playbook.block
from ansible.playbook.block import Block

@pytest.fixture
def block_instance():
    block = Block()
    block._valid_attrs = ['attr1', 'attr2', 'block', 'rescue', 'always']
    block.attr1 = 'value1'
    block.attr2 = 'value2'
    block._role = Mock()
    block._role.serialize.return_value = 'role_serialized'
    block._parent = Mock()
    block._parent.copy.return_value.serialize.return_value = 'parent_serialized'
    block._parent.__class__.__name__ = 'ParentClass'
    return block

def test_serialize_no_role_no_parent(block_instance):
    block_instance._role = None
    block_instance._parent = None
    serialized_data = block_instance.serialize()
    assert serialized_data == {
        'attr1': 'value1',
        'attr2': 'value2',
        'dep_chain': block_instance.get_dep_chain()
    }

def test_serialize_with_role_no_parent(block_instance):
    block_instance._parent = None
    serialized_data = block_instance.serialize()
    assert serialized_data == {
        'attr1': 'value1',
        'attr2': 'value2',
        'dep_chain': block_instance.get_dep_chain(),
        'role': 'role_serialized'
    }

def test_serialize_no_role_with_parent(block_instance):
    block_instance._role = None
    serialized_data = block_instance.serialize()
    assert serialized_data == {
        'attr1': 'value1',
        'attr2': 'value2',
        'dep_chain': block_instance.get_dep_chain(),
        'parent': 'parent_serialized',
        'parent_type': 'ParentClass'
    }

def test_serialize_with_role_with_parent(block_instance):
    serialized_data = block_instance.serialize()
    assert serialized_data == {
        'attr1': 'value1',
        'attr2': 'value2',
        'dep_chain': block_instance.get_dep_chain(),
        'role': 'role_serialized',
        'parent': 'parent_serialized',
        'parent_type': 'ParentClass'
    }
