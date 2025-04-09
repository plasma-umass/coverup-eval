# file: lib/ansible/playbook/block.py:398-411
# asked: {"lines": [398, 405, 406, 407, 408, 409, 411], "branches": [[406, 407], [406, 411], [407, 408], [407, 409]]}
# gained: {"lines": [398, 405, 406, 407, 408, 409, 411], "branches": [[406, 407], [406, 411], [407, 408], [407, 409]]}

import pytest
from unittest.mock import Mock, patch

# Assuming the Block class and its dependencies are imported correctly
from ansible.playbook.block import Block
from ansible.playbook.task_include import TaskInclude

@pytest.fixture
def block_with_parent():
    parent_block = Mock(spec=Block)
    block = Block()
    block._parent = parent_block
    return block, parent_block

@pytest.fixture
def block_with_task_include_parent():
    parent_task_include = Mock(spec=TaskInclude)
    block = Block()
    block._parent = parent_task_include
    return block, parent_task_include

def test_all_parents_static_no_parent():
    block = Block()
    block._parent = None
    assert block.all_parents_static() == True

def test_all_parents_static_parent_block(block_with_parent):
    block, parent_block = block_with_parent
    parent_block.all_parents_static.return_value = True
    assert block.all_parents_static() == True
    parent_block.all_parents_static.assert_called_once()

def test_all_parents_static_parent_task_include_statically_loaded(block_with_task_include_parent):
    block, parent_task_include = block_with_task_include_parent
    parent_task_include.statically_loaded = True
    parent_task_include.all_parents_static.return_value = True
    assert block.all_parents_static() == True
    parent_task_include.all_parents_static.assert_called_once()

def test_all_parents_static_parent_task_include_not_statically_loaded(block_with_task_include_parent):
    block, parent_task_include = block_with_task_include_parent
    parent_task_include.statically_loaded = False
    assert block.all_parents_static() == False
