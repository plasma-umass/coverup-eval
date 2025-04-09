# file: lib/ansible/playbook/block.py:119-132
# asked: {"lines": [119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 131, 132], "branches": []}
# gained: {"lines": [119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 131, 132], "branches": []}

import pytest
from unittest.mock import Mock, patch
from ansible.playbook.block import Block
from ansible.errors import AnsibleParserError

@pytest.fixture
def block_instance():
    return Block()

def test_load_block_success(block_instance, mocker):
    mock_load_list_of_tasks = mocker.patch('ansible.playbook.block.load_list_of_tasks', return_value='mocked_tasks')
    ds = 'mocked_ds'
    result = block_instance._load_block('attr', ds)
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
    assert result == 'mocked_tasks'

def test_load_block_failure(block_instance, mocker):
    mock_load_list_of_tasks = mocker.patch('ansible.playbook.block.load_list_of_tasks', side_effect=AssertionError)
    ds = 'mocked_ds'
    block_instance._ds = ds
    with pytest.raises(AnsibleParserError) as excinfo:
        block_instance._load_block('attr', ds)
    assert str(excinfo.value).strip() == "A malformed block was encountered while loading a block."
    assert excinfo.value.obj == ds
    assert isinstance(excinfo.value.orig_exc, AssertionError)
