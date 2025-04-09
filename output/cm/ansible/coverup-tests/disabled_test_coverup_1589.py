# file lib/ansible/playbook/block.py:398-411
# lines [405, 406, 407, 408, 409, 411]
# branches ['406->407', '406->411', '407->408', '407->409']

import pytest
from ansible.playbook.block import Block
from ansible.playbook.task_include import TaskInclude

@pytest.fixture
def mock_task_include(mocker):
    task_include = mocker.MagicMock(spec=TaskInclude)
    task_include.statically_loaded = False
    return task_include

@pytest.fixture
def mock_block(mocker, mock_task_include):
    block = mocker.MagicMock(spec=Block)
    block._parent = mock_task_include
    block.all_parents_static.return_value = True
    return block

def test_all_parents_static_with_task_include_parent(mock_block, mock_task_include):
    block = Block()
    block._parent = mock_task_include
    assert not block.all_parents_static()

def test_all_parents_static_with_block_parent(mock_block):
    block = Block()
    block._parent = mock_block
    assert block.all_parents_static()
