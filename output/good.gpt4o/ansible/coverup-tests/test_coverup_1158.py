# file lib/ansible/playbook/block.py:398-411
# lines [405, 406, 407, 408, 409, 411]
# branches ['406->407', '406->411', '407->408', '407->409']

import pytest
from unittest.mock import Mock, patch

# Assuming the Block class and its dependencies are imported correctly
from ansible.playbook.block import Block
from ansible.playbook.task_include import TaskInclude

@pytest.fixture
def mock_task_include():
    return Mock(spec=TaskInclude)

@pytest.fixture
def mock_block():
    return Mock(spec=Block)

def test_all_parents_static_with_task_include(mock_task_include, mock_block):
    # Setup the mock parent TaskInclude
    mock_task_include.statically_loaded = False
    mock_block._parent = mock_task_include

    block_instance = Block()
    block_instance._parent = mock_block

    # Test when parent is TaskInclude and not statically loaded
    block_instance._parent = mock_task_include
    assert not block_instance.all_parents_static()

    # Test when parent is TaskInclude and statically loaded
    mock_task_include.statically_loaded = True
    assert block_instance.all_parents_static()

def test_all_parents_static_with_block(mock_block):
    # Setup the mock parent Block
    mock_block.all_parents_static.return_value = True

    block_instance = Block()
    block_instance._parent = mock_block

    # Test when parent is another Block
    assert block_instance.all_parents_static()

def test_all_parents_static_no_parent():
    block_instance = Block()
    block_instance._parent = None

    # Test when there is no parent
    assert block_instance.all_parents_static()
