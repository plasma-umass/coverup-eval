# file: lib/ansible/playbook/block.py:119-132
# asked: {"lines": [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 131, 132], "branches": []}
# gained: {"lines": [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 131, 132], "branches": []}

import pytest
from unittest.mock import Mock, patch
from ansible.playbook.block import Block
from ansible.errors import AnsibleParserError

@pytest.fixture
def mock_block():
    block = Block()
    block._play = Mock()
    block._role = Mock()
    block._variable_manager = Mock()
    block._loader = Mock()
    block._use_handlers = Mock()
    block._ds = Mock()
    return block

@patch('ansible.playbook.block.load_list_of_tasks')
def test_load_block_success(mock_load_list_of_tasks, mock_block):
    mock_load_list_of_tasks.return_value = ['task1', 'task2']
    result = mock_block._load_block('attr', 'ds')
    assert result == ['task1', 'task2']
    mock_load_list_of_tasks.assert_called_once_with(
        'ds',
        play=mock_block._play,
        block=mock_block,
        role=mock_block._role,
        task_include=None,
        variable_manager=mock_block._variable_manager,
        loader=mock_block._loader,
        use_handlers=mock_block._use_handlers,
    )

@patch('ansible.playbook.block.load_list_of_tasks')
def test_load_block_failure(mock_load_list_of_tasks, mock_block):
    mock_load_list_of_tasks.side_effect = AssertionError("Test error")
    with pytest.raises(AnsibleParserError) as excinfo:
        mock_block._load_block('attr', 'ds')
    assert "A malformed block was encountered while loading a block" in str(excinfo.value)
    assert excinfo.value.obj == mock_block._ds
    assert isinstance(excinfo.value.orig_exc, AssertionError)
    mock_load_list_of_tasks.assert_called_once_with(
        'ds',
        play=mock_block._play,
        block=mock_block,
        role=mock_block._role,
        task_include=None,
        variable_manager=mock_block._variable_manager,
        loader=mock_block._loader,
        use_handlers=mock_block._use_handlers,
    )
