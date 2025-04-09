# file: lib/ansible/playbook/block.py:413-419
# asked: {"lines": [413, 414, 415, 416, 417, 418, 419], "branches": [[415, 416], [415, 419], [416, 417], [416, 418]]}
# gained: {"lines": [413, 414, 415, 416, 417, 418, 419], "branches": [[415, 416], [415, 419], [416, 417], [416, 418]]}

import pytest
from unittest.mock import Mock, patch
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

def test_get_first_parent_include_parent_is_task_include():
    block = Block()
    task_include_mock = Mock(spec=TaskInclude)
    block._parent = task_include_mock
    assert block.get_first_parent_include() is task_include_mock

def test_get_first_parent_include_parent_is_not_task_include(block_with_parent):
    block, parent_mock = block_with_parent
    parent_mock.get_first_parent_include.return_value = 'parent_include'
    assert block.get_first_parent_include() == 'parent_include'
    parent_mock.get_first_parent_include.assert_called_once()

def test_get_first_parent_include_nested_task_include():
    block = Block()
    parent_block = Block()
    task_include_mock = Mock(spec=TaskInclude)
    parent_block._parent = task_include_mock
    block._parent = parent_block
    assert block.get_first_parent_include() is task_include_mock
