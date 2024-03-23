# file lib/ansible/playbook/block.py:413-419
# lines [414, 415, 416, 417, 418, 419]
# branches ['415->416', '415->419', '416->417', '416->418']

import pytest
from ansible.playbook.block import Block
from ansible.playbook.task_include import TaskInclude

# Mock class to simulate a parent that is not a TaskInclude
class MockParent:
    def get_first_parent_include(self):
        return None

@pytest.fixture
def block_with_task_include_parent(mocker):
    block = Block()
    task_include_parent = TaskInclude()
    block._parent = task_include_parent
    return block

@pytest.fixture
def block_with_non_task_include_parent(mocker):
    block = Block()
    non_task_include_parent = MockParent()
    block._parent = non_task_include_parent
    return block

@pytest.fixture
def block_with_no_parent(mocker):
    block = Block()
    block._parent = None
    return block

def test_get_first_parent_include_with_task_include_parent(block_with_task_include_parent):
    assert block_with_task_include_parent.get_first_parent_include() is block_with_task_include_parent._parent

def test_get_first_parent_include_with_non_task_include_parent(block_with_non_task_include_parent):
    assert block_with_non_task_include_parent.get_first_parent_include() is None

def test_get_first_parent_include_with_no_parent(block_with_no_parent):
    assert block_with_no_parent.get_first_parent_include() is None
