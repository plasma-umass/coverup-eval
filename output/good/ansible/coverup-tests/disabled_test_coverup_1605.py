# file lib/ansible/playbook/block.py:413-419
# lines [414, 415, 416, 417, 418, 419]
# branches ['415->416', '415->419', '416->417', '416->418']

import pytest
from ansible.playbook.block import Block

# Mock classes to simulate the behavior of actual classes
class MockTaskInclude:
    pass

class MockParentBlock:
    def get_first_parent_include(self):
        return MockTaskInclude()

# Test function to cover lines 414-419
def test_get_first_parent_include(mocker):
    # Mock the TaskInclude class
    mocker.patch('ansible.playbook.task_include.TaskInclude', new=MockTaskInclude)

    # Create a Block instance with a MockParentBlock as its parent
    block_with_parent = Block()
    block_with_parent._parent = MockParentBlock()

    # Create a Block instance with a MockTaskInclude as its parent
    block_with_task_include_parent = Block()
    block_with_task_include_parent._parent = MockTaskInclude()

    # Create a Block instance with no parent
    block_with_no_parent = Block()
    block_with_no_parent._parent = None

    # Assert that get_first_parent_include returns the correct type
    assert isinstance(block_with_parent.get_first_parent_include(), MockTaskInclude)
    assert isinstance(block_with_task_include_parent.get_first_parent_include(), MockTaskInclude)
    assert block_with_no_parent.get_first_parent_include() is None
