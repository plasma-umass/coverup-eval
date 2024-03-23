# file lib/ansible/playbook/block.py:413-419
# lines [413, 414, 415, 416, 417, 418, 419]
# branches ['415->416', '415->419', '416->417', '416->418']

import pytest
from ansible.playbook.block import Block
from ansible.playbook.task_include import TaskInclude

# Mock classes to simulate the behavior of actual classes
class MockBase:
    pass

class MockConditional:
    pass

class MockCollectionSearch:
    pass

class MockTaggable:
    pass

# Inheriting from the mock classes instead of the actual ones to isolate the test
class MockBlock(MockBase, MockConditional, MockCollectionSearch, MockTaggable, Block):
    pass

class MockTaskInclude(TaskInclude):
    pass

# Test function to cover get_first_parent_include method
def test_get_first_parent_include(mocker):
    # Create a mock TaskInclude object
    mock_task_include = mocker.Mock(spec=MockTaskInclude)
    
    # Create a Block object with a parent that is a TaskInclude
    block_with_task_include_parent = MockBlock()
    block_with_task_include_parent._parent = mock_task_include
    
    # Assert that get_first_parent_include returns the TaskInclude parent
    assert block_with_task_include_parent.get_first_parent_include() is mock_task_include
    
    # Create a Block object with a parent that is another Block
    block_with_block_parent = MockBlock()
    block_with_block_parent._parent = MockBlock()
    
    # Mock the get_first_parent_include method of the parent block to return a TaskInclude
    block_with_block_parent._parent.get_first_parent_include = mocker.Mock(return_value=mock_task_include)
    
    # Assert that get_first_parent_include returns the TaskInclude from the parent's get_first_parent_include
    assert block_with_block_parent.get_first_parent_include() is mock_task_include
    
    # Create a Block object with no parent
    block_with_no_parent = MockBlock()
    block_with_no_parent._parent = None
    
    # Assert that get_first_parent_include returns None when there is no parent
    assert block_with_no_parent.get_first_parent_include() is None

# Ensure that the test function is recognized by pytest
test_get_first_parent_include.__test__ = True
