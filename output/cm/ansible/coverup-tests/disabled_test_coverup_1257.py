# file lib/ansible/playbook/block.py:398-411
# lines [405, 406, 407, 408, 409, 411]
# branches ['406->407', '406->411', '407->408', '407->409']

import pytest
from ansible.playbook.block import Block
from ansible.playbook.task_include import TaskInclude

@pytest.fixture
def mock_task_include(mocker):
    task_include = TaskInclude()
    task_include.statically_loaded = False
    return task_include

@pytest.fixture
def mock_block(mocker, mock_task_include):
    block = Block()
    block._parent = mock_task_include
    return block

def test_all_parents_static(mock_block):
    assert not mock_block.all_parents_static(), "Expected all_parents_static to return False when parent is a TaskInclude and not statically loaded"

    # Cleanup is handled by pytest fixtures automatically
