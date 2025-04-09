# file: lib/ansible/playbook/block.py:50-63
# asked: {"lines": [50, 51, 52, 53, 54, 55, 56, 58, 59, 60, 61, 63], "branches": [[58, 59], [58, 60], [60, 61], [60, 63]]}
# gained: {"lines": [50, 51, 52, 53, 54, 55, 56, 58, 59, 60, 61, 63], "branches": [[58, 59], [58, 60], [60, 61], [60, 63]]}

import pytest
from ansible.playbook.block import Block

def test_block_init_with_task_include():
    play = "play"
    role = "role"
    task_include = "task_include"
    block = Block(play=play, role=role, task_include=task_include)
    
    assert block._play == play
    assert block._role == role
    assert block._parent == task_include
    assert block._use_handlers is False
    assert block._implicit is False

def test_block_init_with_parent_block():
    play = "play"
    role = "role"
    parent_block = "parent_block"
    block = Block(play=play, role=role, parent_block=parent_block)
    
    assert block._play == play
    assert block._role == role
    assert block._parent == parent_block
    assert block._use_handlers is False
    assert block._implicit is False

def test_block_init_with_neither():
    play = "play"
    role = "role"
    block = Block(play=play, role=role)
    
    assert block._play == play
    assert block._role == role
    assert block._parent is None
    assert block._use_handlers is False
    assert block._implicit is False

def test_block_init_with_use_handlers_and_implicit():
    play = "play"
    role = "role"
    block = Block(play=play, role=role, use_handlers=True, implicit=True)
    
    assert block._play == play
    assert block._role == role
    assert block._parent is None
    assert block._use_handlers is True
    assert block._implicit is True
