# file: lib/ansible/playbook/block.py:398-411
# asked: {"lines": [398, 405, 406, 407, 408, 409, 411], "branches": [[406, 407], [406, 411], [407, 408], [407, 409]]}
# gained: {"lines": [398, 405, 406, 407, 408, 409, 411], "branches": [[406, 407], [406, 411], [407, 408], [407, 409]]}

import pytest
from ansible.playbook.block import Block
from ansible.playbook.task_include import TaskInclude

def test_all_parents_static_with_no_parent():
    block = Block()
    assert block.all_parents_static() == True

def test_all_parents_static_with_task_include_parent():
    task_include = TaskInclude()
    block = Block(task_include=task_include)
    assert block.all_parents_static() == False

def test_all_parents_static_with_statically_loaded_task_include_parent():
    task_include = TaskInclude()
    task_include.statically_loaded = True
    block = Block(task_include=task_include)
    assert block.all_parents_static() == True

def test_all_parents_static_with_block_parent():
    parent_block = Block()
    block = Block(parent_block=parent_block)
    assert block.all_parents_static() == True

def test_all_parents_static_with_nested_task_include_parent():
    task_include = TaskInclude()
    parent_block = Block(task_include=task_include)
    block = Block(parent_block=parent_block)
    assert block.all_parents_static() == False

def test_all_parents_static_with_nested_statically_loaded_task_include_parent():
    task_include = TaskInclude()
    task_include.statically_loaded = True
    parent_block = Block(task_include=task_include)
    block = Block(parent_block=parent_block)
    assert block.all_parents_static() == True
