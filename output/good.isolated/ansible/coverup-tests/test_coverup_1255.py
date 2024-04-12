# file lib/ansible/playbook/block.py:134-147
# lines [135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 146, 147]
# branches []

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.block import Block
from ansible.playbook.role import Role
from ansible.playbook.play import Play
from ansible.vars.manager import VariableManager
from ansible.parsing.dataloader import DataLoader

# Mock the necessary components to test Block._load_rescue
class TestBlock:
    @pytest.fixture
    def mock_play(self, mocker):
        return mocker.MagicMock(spec=Play)

    @pytest.fixture
    def mock_role(self, mocker):
        return mocker.MagicMock(spec=Role)

    @pytest.fixture
    def mock_variable_manager(self, mocker):
        return mocker.MagicMock(spec=VariableManager)

    @pytest.fixture
    def mock_loader(self, mocker):
        return mocker.MagicMock(spec=DataLoader)

    @pytest.fixture
    def block_instance(self, mock_play, mock_role, mock_variable_manager, mock_loader):
        block = Block(play=mock_play, role=mock_role)
        block._variable_manager = mock_variable_manager
        block._loader = mock_loader
        return block

    def test_load_rescue_with_malformed_block(self, block_instance, mocker):
        # Mock the load_list_of_tasks to raise an AssertionError
        mocker.patch('ansible.playbook.block.load_list_of_tasks', side_effect=AssertionError("Malformed block"))

        # Define a malformed data structure to trigger the exception
        malformed_ds = {'rescue': None}

        # Set the block's _ds attribute to the malformed data structure
        block_instance._ds = malformed_ds

        # Expect AnsibleParserError to be raised due to the malformed block
        with pytest.raises(AnsibleParserError) as excinfo:
            block_instance._load_rescue('rescue', malformed_ds)

        # Check if the exception message matches the expected message
        assert "A malformed block was encountered while loading rescue." in str(excinfo.value)
