# file lib/ansible/playbook/block.py:149-162
# lines [149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 161, 162]
# branches []

import pytest
from ansible.playbook.block import Block
from ansible.errors import AnsibleParserError
from unittest.mock import Mock, patch

@pytest.fixture
def mock_load_list_of_tasks(mocker):
    return mocker.patch('ansible.playbook.block.load_list_of_tasks')

@pytest.fixture
def block_instance():
    block = Block()
    block._ds = {'some': 'data'}  # Mocking the _ds attribute
    block._play = Mock()
    block._role = Mock()
    block._variable_manager = Mock()
    block._loader = Mock()
    block._use_handlers = Mock()
    return block

def test_load_always_success(mock_load_list_of_tasks, block_instance):
    mock_load_list_of_tasks.return_value = ['task1', 'task2']
    ds = {'some': 'data'}
    result = block_instance._load_always('attr', ds)
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

def test_load_always_failure(mock_load_list_of_tasks, block_instance):
    mock_load_list_of_tasks.side_effect = AssertionError("Test error")
    ds = {'some': 'data'}
    with pytest.raises(AnsibleParserError) as excinfo:
        block_instance._load_always('attr', ds)
    assert "A malformed block was encountered while loading always" in str(excinfo.value)
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
