# file lib/ansible/playbook/play.py:183-191
# lines [183, 188, 189, 190, 191]
# branches []

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.play import Play
from ansible.playbook.block import Block
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from unittest.mock import MagicMock, create_autospec

# Mocking the necessary parts to test Play._load_post_tasks
@pytest.fixture
def mock_load_list_of_blocks(mocker):
    return mocker.patch('ansible.playbook.play.load_list_of_blocks', return_value=[Block()])

@pytest.fixture
def mock_variable_manager():
    return create_autospec(VariableManager)

@pytest.fixture
def mock_loader():
    return create_autospec(DataLoader)

@pytest.fixture
def play(mock_variable_manager, mock_loader):
    mock_play = Play()
    mock_play._variable_manager = mock_variable_manager
    mock_play._loader = mock_loader
    mock_play._ds = {}  # Add a _ds attribute to the mock Play object
    return mock_play

def test_load_post_tasks_with_valid_data(play, mock_load_list_of_blocks):
    # Arrange
    ds = [{'block': 'test'}]

    # Act
    result = play._load_post_tasks(attr=None, ds=ds)

    # Assert
    assert result == mock_load_list_of_blocks.return_value
    mock_load_list_of_blocks.assert_called_once_with(ds=ds, play=play, variable_manager=play._variable_manager, loader=play._loader)

def test_load_post_tasks_with_invalid_data_raises_exception(play, mocker):
    # Arrange
    mocker.patch('ansible.playbook.play.load_list_of_blocks', side_effect=AssertionError("Invalid block"))
    ds = [{'invalid': 'data'}]

    # Act & Assert
    with pytest.raises(AnsibleParserError) as exc_info:
        play._load_post_tasks(attr=None, ds=ds)

    assert "A malformed block was encountered while loading post_tasks" in str(exc_info.value)
    assert exc_info.value.orig_exc is not None
