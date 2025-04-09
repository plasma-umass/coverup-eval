# file lib/ansible/playbook/block.py:119-132
# lines [119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 131, 132]
# branches []

import pytest
from unittest.mock import Mock, patch
from ansible.playbook.block import Block
from ansible.errors import AnsibleParserError

@pytest.fixture
def mock_load_list_of_tasks(mocker):
    return mocker.patch('ansible.playbook.block.load_list_of_tasks')

@pytest.fixture
def block_instance():
    block = Block()
    block._play = Mock()
    block._role = Mock()
    block._variable_manager = Mock()
    block._loader = Mock()
    block._use_handlers = Mock()
    block._ds = Mock()
    return block

def test_load_block_success(block_instance, mock_load_list_of_tasks):
    mock_load_list_of_tasks.return_value = ['task1', 'task2']
    ds = ['task_data']
    result = block_instance._load_block('attr', ds)
    assert result == ['task1', 'task2']
    mock_load_list_of_tasks.assert_called_once_with(
        ds,
        play=block_instance._play,
        block=block_instance,
        role=block_instance._role,
        task_include=None,
        variable_manager=block_instance._variable_manager,
        loader=block_instance._loader,
        use_handlers=block_instance._use_handlers,
    )

def test_load_block_failure(block_instance, mock_load_list_of_tasks):
    mock_load_list_of_tasks.side_effect = AssertionError("Test error")
    ds = ['task_data']
    with pytest.raises(AnsibleParserError) as excinfo:
        block_instance._load_block('attr', ds)
    assert "A malformed block was encountered while loading a block" in str(excinfo.value)
    assert excinfo.value.obj == block_instance._ds
    assert isinstance(excinfo.value.orig_exc, AssertionError)
    mock_load_list_of_tasks.assert_called_once_with(
        ds,
        play=block_instance._play,
        block=block_instance,
        role=block_instance._role,
        task_include=None,
        variable_manager=block_instance._variable_manager,
        loader=block_instance._loader,
        use_handlers=block_instance._use_handlers,
    )
