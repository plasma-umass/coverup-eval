# file: lib/ansible/playbook/block.py:89-93
# asked: {"lines": [91, 92, 93], "branches": []}
# gained: {"lines": [91, 92, 93], "branches": []}

import pytest
from ansible.playbook.block import Block

@pytest.fixture
def mock_block(mocker):
    mocker.patch('ansible.playbook.block.Block.is_block', return_value=False)
    mocker.patch('ansible.playbook.block.Block.load_data', return_value='mocked_load_data')
    return Block

def test_block_load_with_implicit_false(mock_block):
    data = {'some': 'data'}
    play = 'play'
    parent_block = 'parent_block'
    role = 'role'
    task_include = 'task_include'
    use_handlers = True
    variable_manager = 'variable_manager'
    loader = 'loader'

    result = mock_block.load(data, play=play, parent_block=parent_block, role=role, task_include=task_include, use_handlers=use_handlers, variable_manager=variable_manager, loader=loader)

    assert result == 'mocked_load_data'
    mock_block.is_block.assert_called_once_with(data)
    mock_block.load_data.assert_called_once_with(data, variable_manager=variable_manager, loader=loader)

def test_block_load_with_implicit_true(mocker):
    mocker.patch('ansible.playbook.block.Block.is_block', return_value=True)
    mocker.patch('ansible.playbook.block.Block.load_data', return_value='mocked_load_data')
    data = {'some': 'data'}
    play = 'play'
    parent_block = 'parent_block'
    role = 'role'
    task_include = 'task_include'
    use_handlers = True
    variable_manager = 'variable_manager'
    loader = 'loader'

    result = Block.load(data, play=play, parent_block=parent_block, role=role, task_include=task_include, use_handlers=use_handlers, variable_manager=variable_manager, loader=loader)

    assert result == 'mocked_load_data'
    Block.is_block.assert_called_once_with(data)
    Block.load_data.assert_called_once_with(data, variable_manager=variable_manager, loader=loader)
