# file lib/ansible/playbook/play.py:173-181
# lines [178, 179, 180, 181]
# branches []

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.play import Play
from ansible.playbook.block import Block

# Assuming that load_list_of_blocks is a function that needs to be mocked
# and that it raises an AssertionError when a malformed block is encountered.

@pytest.fixture
def mock_load_list_of_blocks(mocker):
    return mocker.patch('ansible.playbook.play.load_list_of_blocks', side_effect=AssertionError("malformed block"))

@pytest.fixture
def mock_variable_manager(mocker):
    return mocker.Mock()

@pytest.fixture
def mock_loader(mocker):
    return mocker.Mock()

def test_load_pre_tasks_with_malformed_block(mock_load_list_of_blocks, mock_variable_manager, mock_loader):
    play = Play()
    play._variable_manager = mock_variable_manager
    play._loader = mock_loader
    play._ds = {'pre_tasks': [{'malformed': 'block'}]}  # Example of a malformed block

    with pytest.raises(AnsibleParserError) as excinfo:
        play._load_pre_tasks('pre_tasks', play._ds['pre_tasks'])

    assert "A malformed block was encountered while loading pre_tasks" in str(excinfo.value)
    assert excinfo.value.obj == play._ds
    assert isinstance(excinfo.value.orig_exc, AssertionError)
