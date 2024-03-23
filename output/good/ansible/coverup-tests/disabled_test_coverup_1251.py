# file lib/ansible/playbook/block.py:119-132
# lines [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 131, 132]
# branches []

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.block import Block
from ansible.playbook.role import Role
from ansible.playbook.play import Play
from ansible.vars.manager import VariableManager
from ansible.parsing.dataloader import DataLoader

# Mock the necessary components to test the Block class
@pytest.fixture
def mock_play(mocker):
    return mocker.MagicMock(spec=Play)

@pytest.fixture
def mock_role(mocker):
    return mocker.MagicMock(spec=Role)

@pytest.fixture
def mock_variable_manager(mocker):
    return mocker.MagicMock(spec=VariableManager)

@pytest.fixture
def mock_loader(mocker):
    return mocker.MagicMock(spec=DataLoader)

@pytest.fixture
def block_instance(mock_play, mock_role, mock_variable_manager, mock_loader):
    # Adjust the Block instantiation to match the expected signature
    # Since the error indicates unexpected keyword arguments, we need to remove them
    return Block()

# Test function to cover lines 120-132
def test_load_block_with_malformed_block(block_instance, mocker):
    # Mock the load_list_of_tasks to raise an AssertionError
    mocker.patch('ansible.playbook.block.load_list_of_tasks', side_effect=AssertionError("malformed block"))

    # Define a malformed data structure
    malformed_ds = {'block': None}

    # Set the _ds attribute to the malformed data structure
    block_instance._ds = malformed_ds

    # Mock the attributes that are expected to be used in the _load_block method
    block_instance._play = mock_play
    block_instance._role = mock_role
    block_instance._loader = mock_loader
    block_instance._use_handlers = False

    # Verify that AnsibleParserError is raised with the expected message
    with pytest.raises(AnsibleParserError) as excinfo:
        block_instance._load_block('block', malformed_ds)
    assert "A malformed block was encountered while loading a block" in str(excinfo.value)
