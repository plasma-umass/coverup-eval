# file: lib/ansible/playbook/block.py:398-411
# asked: {"lines": [405, 406, 407, 408, 409, 411], "branches": [[406, 407], [406, 411], [407, 408], [407, 409]]}
# gained: {"lines": [405, 406, 407, 408, 409, 411], "branches": [[406, 407], [406, 411], [407, 408], [407, 409]]}

import pytest
from unittest.mock import Mock, patch

# Assuming the Block class and its dependencies are imported correctly
from ansible.playbook.block import Block
from ansible.playbook.task_include import TaskInclude

@pytest.fixture
def mock_parent():
    return Mock(spec=Block)

@pytest.fixture
def mock_task_include():
    return Mock(spec=TaskInclude)

def test_all_parents_static_no_parent():
    block = Block()
    block._parent = None
    assert block.all_parents_static() == True

def test_all_parents_static_parent_not_statically_loaded(mock_task_include):
    block = Block()
    mock_task_include.statically_loaded = False
    block._parent = mock_task_include
    assert block.all_parents_static() == False

def test_all_parents_static_parent_statically_loaded(mock_task_include):
    block = Block()
    mock_task_include.statically_loaded = True
    block._parent = mock_task_include
    with patch.object(mock_task_include, 'all_parents_static', return_value=True):
        assert block.all_parents_static() == True

def test_all_parents_static_parent_block(mock_parent):
    block = Block()
    block._parent = mock_parent
    with patch.object(mock_parent, 'all_parents_static', return_value=True):
        assert block.all_parents_static() == True

def test_all_parents_static_parent_block_false(mock_parent):
    block = Block()
    block._parent = mock_parent
    with patch.object(mock_parent, 'all_parents_static', return_value=False):
        assert block.all_parents_static() == False
