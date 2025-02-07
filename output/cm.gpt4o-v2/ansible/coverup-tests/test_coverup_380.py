# file: lib/ansible/playbook/block.py:413-419
# asked: {"lines": [413, 414, 415, 416, 417, 418, 419], "branches": [[415, 416], [415, 419], [416, 417], [416, 418]]}
# gained: {"lines": [413, 414, 415, 416, 417, 418, 419], "branches": [[415, 416], [415, 419], [416, 417], [416, 418]]}

import pytest
from ansible.playbook.block import Block
from ansible.playbook.task_include import TaskInclude

def test_get_first_parent_include_with_task_include():
    task_include = TaskInclude()
    block = Block(task_include=task_include)
    assert block.get_first_parent_include() == task_include

def test_get_first_parent_include_with_parent_block(mocker):
    parent_block = mocker.Mock(spec=Block)
    parent_block.get_first_parent_include.return_value = 'parent_include'
    block = Block(parent_block=parent_block)
    assert block.get_first_parent_include() == 'parent_include'
    parent_block.get_first_parent_include.assert_called_once()

def test_get_first_parent_include_with_no_parent():
    block = Block()
    assert block.get_first_parent_include() is None
