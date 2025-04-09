# file lib/ansible/playbook/block.py:245-281
# lines [245, 252, 253, 257, 258, 259, 261, 264, 265, 266, 267, 268, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281]
# branches ['257->258', '257->261', '258->257', '258->259', '265->266', '265->270', '271->exit', '271->272', '273->274', '273->275', '275->276', '275->277', '277->278', '277->279']

import pytest
from ansible.playbook.block import Block
from ansible.playbook.role import Role
from ansible.playbook.task_include import TaskInclude
from ansible.playbook.handler_task_include import HandlerTaskInclude

@pytest.fixture
def block_data():
    return {
        'block': None,
        'rescue': None,
        'always': None,
        'dep_chain': 'test_dep_chain',
        'role': {'name': 'test_role'},
        'parent': {'dummy_key': 'dummy_value'},
        'parent_type': 'Block'
    }

@pytest.fixture
def task_include_data():
    return {
        'parent': {'dummy_key': 'dummy_value'},
        'parent_type': 'TaskInclude'
    }

@pytest.fixture
def handler_task_include_data():
    return {
        'parent': {'dummy_key': 'dummy_value'},
        'parent_type': 'HandlerTaskInclude'
    }

def test_block_deserialize_with_role(block_data):
    block = Block()
    block.deserialize(block_data)
    assert isinstance(block._role, Role)
    # The dep_chain should be set from the parent if parent is present
    assert block._dep_chain == block._parent.get_dep_chain()

def test_block_deserialize_with_block_parent(block_data):
    block = Block()
    block.deserialize(block_data)
    assert isinstance(block._parent, Block)
    assert block._dep_chain == block._parent.get_dep_chain()

def test_block_deserialize_with_task_include_parent(task_include_data):
    block = Block()
    block.deserialize(task_include_data)
    assert isinstance(block._parent, TaskInclude)

def test_block_deserialize_with_handler_task_include_parent(handler_task_include_data):
    block = Block()
    block.deserialize(handler_task_include_data)
    assert isinstance(block._parent, HandlerTaskInclude)
