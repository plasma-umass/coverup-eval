# file: lib/ansible/playbook/block.py:149-162
# asked: {"lines": [149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 161, 162], "branches": []}
# gained: {"lines": [149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 161, 162], "branches": []}

import pytest
from unittest.mock import Mock, patch
from ansible.playbook.block import Block
from ansible.errors import AnsibleParserError

@pytest.fixture
def mock_load_list_of_tasks():
    with patch('ansible.playbook.block.load_list_of_tasks') as mock:
        yield mock

@pytest.fixture
def block_instance():
    block = Block(play=Mock(), parent_block=Mock(), role=Mock(), task_include=Mock(), use_handlers=False, implicit=False)
    block._ds = Mock()  # Mock the _ds attribute
    block._variable_manager = Mock()  # Mock the _variable_manager attribute
    block._loader = Mock()  # Mock the _loader attribute
    return block

def test_load_always_success(block_instance, mock_load_list_of_tasks):
    mock_load_list_of_tasks.return_value = ['task1', 'task2']
    result = block_instance._load_always('attr', ['task_ds'])
    assert result == ['task1', 'task2']
    mock_load_list_of_tasks.assert_called_once_with(
        ['task_ds'],
        play=block_instance._play,
        block=block_instance,
        role=block_instance._role,
        task_include=None,
        variable_manager=block_instance._variable_manager,
        loader=block_instance._loader,
        use_handlers=block_instance._use_handlers,
    )

def test_load_always_failure(block_instance, mock_load_list_of_tasks):
    mock_load_list_of_tasks.side_effect = AssertionError("Test AssertionError")
    with pytest.raises(AnsibleParserError) as excinfo:
        block_instance._load_always('attr', ['task_ds'])
    assert str(excinfo.value) == "A malformed block was encountered while loading always. Test AssertionError"
    assert excinfo.value.obj == block_instance._ds
    assert isinstance(excinfo.value.orig_exc, AssertionError)
    mock_load_list_of_tasks.assert_called_once_with(
        ['task_ds'],
        play=block_instance._play,
        block=block_instance,
        role=block_instance._role,
        task_include=None,
        variable_manager=block_instance._variable_manager,
        loader=block_instance._loader,
        use_handlers=block_instance._use_handlers,
    )
