# file: lib/ansible/playbook/block.py:50-63
# asked: {"lines": [50, 51, 52, 53, 54, 55, 56, 58, 59, 60, 61, 63], "branches": [[58, 59], [58, 60], [60, 61], [60, 63]]}
# gained: {"lines": [50, 51, 52, 53, 54, 55, 56, 58, 59, 60, 61, 63], "branches": [[58, 59], [58, 60], [60, 61], [60, 63]]}

import pytest
from ansible.playbook.block import Block

def test_block_init_with_task_include():
    task_include = "task_include_example"
    block = Block(task_include=task_include)
    assert block._parent == task_include

def test_block_init_with_parent_block():
    parent_block = "parent_block_example"
    block = Block(parent_block=parent_block)
    assert block._parent == parent_block

def test_block_init_without_task_include_or_parent_block():
    block = Block()
    assert block._parent is None
