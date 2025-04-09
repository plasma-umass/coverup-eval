# file: lib/ansible/playbook/block.py:413-419
# asked: {"lines": [413, 414, 415, 416, 417, 418, 419], "branches": [[415, 416], [415, 419], [416, 417], [416, 418]]}
# gained: {"lines": [413, 414, 415, 416, 417, 418, 419], "branches": [[415, 416], [415, 419], [416, 417], [416, 418]]}

import pytest
from unittest.mock import Mock, patch

# Assuming the Block class and its dependencies are imported correctly
from ansible.playbook.block import Block
from ansible.playbook.task_include import TaskInclude

@pytest.fixture
def block_with_parent():
    parent_mock = Mock(spec=Block)
    block = Block()
    block._parent = parent_mock
    return block, parent_mock

def test_get_first_parent_include_no_parent():
    block = Block()
    block._parent = None
    assert block.get_first_parent_include() is None

def test_get_first_parent_include_with_task_include_parent():
    block = Block()
    task_include_parent = Mock(spec=TaskInclude)
    block._parent = task_include_parent
    assert block.get_first_parent_include() == task_include_parent

def test_get_first_parent_include_with_non_task_include_parent(block_with_parent):
    block, parent_mock = block_with_parent
    parent_mock.get_first_parent_include.return_value = 'mocked_value'
    assert block.get_first_parent_include() == 'mocked_value'
    parent_mock.get_first_parent_include.assert_called_once()

def test_get_first_parent_include_nested_task_include():
    block = Block()
    task_include_parent = Mock(spec=TaskInclude)
    intermediate_parent = Mock(spec=Block)
    intermediate_parent._parent = task_include_parent
    block._parent = intermediate_parent

    with patch.object(intermediate_parent, 'get_first_parent_include', return_value=task_include_parent):
        assert block.get_first_parent_include() == task_include_parent
        intermediate_parent.get_first_parent_include.assert_called_once()
