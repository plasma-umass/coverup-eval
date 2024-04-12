# file lib/ansible/playbook/block.py:89-93
# lines [91, 92, 93]
# branches []

import pytest
from ansible.playbook.block import Block

def test_block_load_with_implicit_true(mocker):
    # Mock the dependencies
    play = mocker.MagicMock()
    parent_block = mocker.MagicMock()
    role = mocker.MagicMock()
    task_include = mocker.MagicMock()
    variable_manager = mocker.MagicMock()
    loader = mocker.MagicMock()

    # Mock the is_block static method to return False, making 'implicit' True
    mocker.patch.object(Block, 'is_block', return_value=False)

    # Create a mock Block instance to be returned by load_data
    mock_block_instance = mocker.MagicMock()
    mock_block_instance.implicit = True

    # Mock the load_data method to return our mock Block instance
    mocker.patch.object(Block, 'load_data', return_value=mock_block_instance)

    # Call the method under test
    result = Block.load(data={}, play=play, parent_block=parent_block, role=role, task_include=task_include, use_handlers=False, variable_manager=variable_manager, loader=loader)

    # Assert that the result is our mock Block instance
    assert result == mock_block_instance

    # Assert that is_block was called with the correct data
    Block.is_block.assert_called_once_with({})

    # Assert that load_data was called with the correct parameters
    Block.load_data.assert_called_once_with({}, variable_manager=variable_manager, loader=loader)

    # Assert that the 'implicit' attribute of the result is True
    assert result.implicit is True
