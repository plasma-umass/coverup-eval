# file lib/ansible/playbook/play.py:173-181
# lines [173, 178, 179, 180, 181]
# branches []

import pytest
from unittest.mock import Mock, patch
from ansible.playbook.play import Play
from ansible.errors import AnsibleParserError

@pytest.fixture
def mock_load_list_of_blocks(mocker):
    return mocker.patch('ansible.playbook.play.load_list_of_blocks')

@pytest.fixture
def play_instance():
    mock_variable_manager = Mock()
    mock_loader = Mock()
    play = Play()
    play._variable_manager = mock_variable_manager
    play._loader = mock_loader
    play._ds = {}
    return play

def test_load_pre_tasks_success(play_instance, mock_load_list_of_blocks):
    mock_load_list_of_blocks.return_value = 'expected_result'
    result = play_instance._load_pre_tasks('attr', 'ds')
    assert result == 'expected_result'
    mock_load_list_of_blocks.assert_called_once_with(ds='ds', play=play_instance, variable_manager=play_instance._variable_manager, loader=play_instance._loader)

def test_load_pre_tasks_failure(play_instance, mock_load_list_of_blocks):
    mock_load_list_of_blocks.side_effect = AssertionError('test error')
    with pytest.raises(AnsibleParserError) as excinfo:
        play_instance._load_pre_tasks('attr', 'ds')
    assert str(excinfo.value) == "A malformed block was encountered while loading pre_tasks. test error"
    assert excinfo.value.obj == play_instance._ds
    assert isinstance(excinfo.value.orig_exc, AssertionError)
    mock_load_list_of_blocks.assert_called_once_with(ds='ds', play=play_instance, variable_manager=play_instance._variable_manager, loader=play_instance._loader)
