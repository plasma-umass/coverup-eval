# file lib/ansible/playbook/block.py:89-93
# lines [91, 92, 93]
# branches []

import pytest
from ansible.playbook.block import Block

def test_block_load(mocker):
    # Mocking the Block.is_block method to return False to ensure implicit is True
    mocker.patch('ansible.playbook.block.Block.is_block', return_value=False)
    
    data = {}
    play = mocker.Mock()
    parent_block = mocker.Mock()
    role = mocker.Mock()
    task_include = mocker.Mock()
    use_handlers = mocker.Mock()
    variable_manager = mocker.Mock()
    loader = mocker.Mock()
    
    # Mocking the load_data method to ensure it gets called
    mock_load_data = mocker.patch.object(Block, 'load_data', return_value='mocked_load_data')
    
    result = Block.load(data, play=play, parent_block=parent_block, role=role, task_include=task_include, use_handlers=use_handlers, variable_manager=variable_manager, loader=loader)
    
    # Assertions to verify the expected behavior
    assert result == 'mocked_load_data'
    mock_load_data.assert_called_once_with(data, variable_manager=variable_manager, loader=loader)
    Block.is_block.assert_called_once_with(data)
