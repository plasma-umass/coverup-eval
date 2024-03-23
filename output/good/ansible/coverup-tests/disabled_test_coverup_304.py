# file lib/ansible/playbook/task_include.py:132-151
# lines [132, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 149, 151]
# branches ['138->139', '138->149']

import pytest
from ansible.playbook.task_include import TaskInclude
from ansible.playbook.block import Block
from unittest.mock import MagicMock, create_autospec
from ansible.playbook.role import Role
from ansible.errors import AnsibleParserError

# Mock the necessary components to test TaskInclude
class MockPlay:
    pass

@pytest.fixture
def task_include_fixture():
    # Setup the TaskInclude object with mocks
    task_include = TaskInclude()
    task_include._parent = MagicMock(_play=MockPlay())
    task_include._role = create_autospec(Role, instance=True)
    task_include._variable_manager = MagicMock()
    task_include._loader = MagicMock()
    task_include.args = {'apply': {'name': 'test_block'}}
    return task_include

def test_build_parent_block_with_apply(task_include_fixture):
    # Test the build_parent_block method when 'apply' is in args
    p_block = task_include_fixture.build_parent_block()
    
    # Assertions to check if the block is created correctly
    assert isinstance(p_block, Block), "The parent block should be an instance of Block"
    assert p_block.block == [], "The block attribute should be an empty list"
    assert p_block._play == task_include_fixture._parent._play, "The play attribute should match the parent's play"
    # Removed the assertion for task_include as Block does not have this attribute
    assert 'apply' not in task_include_fixture.args, "The 'apply' key should be popped from the args"

def test_build_parent_block_without_apply(task_include_fixture):
    # Remove 'apply' from args to test the else branch
    task_include_fixture.args.pop('apply')
    
    # Test the build_parent_block method when 'apply' is not in args
    p_block = task_include_fixture.build_parent_block()
    
    # Assertions to check if the block is the TaskInclude itself
    assert p_block == task_include_fixture, "The parent block should be the TaskInclude instance itself when 'apply' is not present"
