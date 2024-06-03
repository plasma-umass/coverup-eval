# file lib/ansible/playbook/play.py:163-171
# lines [163, 168, 169, 170, 171]
# branches []

import pytest
from unittest.mock import Mock, patch
from ansible.playbook.play import Play
from ansible.errors import AnsibleParserError

@pytest.fixture
def mock_load_list_of_blocks(mocker):
    return mocker.patch('ansible.playbook.play.load_list_of_blocks')

def test_load_tasks_success(mock_load_list_of_blocks):
    mock_load_list_of_blocks.return_value = 'mocked_blocks'
    play = Play()
    play._variable_manager = Mock()
    play._loader = Mock()
    ds = [{'name': 'task1'}, {'name': 'task2'}]
    
    result = play._load_tasks('tasks', ds)
    
    assert result == 'mocked_blocks'
    mock_load_list_of_blocks.assert_called_once_with(ds=ds, play=play, variable_manager=play._variable_manager, loader=play._loader)

def test_load_tasks_assertion_error(mock_load_list_of_blocks):
    mock_load_list_of_blocks.side_effect = AssertionError('mocked error')
    play = Play()
    play._variable_manager = Mock()
    play._loader = Mock()
    play._ds = [{'name': 'task1'}, {'name': 'task2'}]
    
    with pytest.raises(AnsibleParserError) as excinfo:
        play._load_tasks('tasks', play._ds)
    
    assert 'A malformed block was encountered while loading tasks: mocked error' in str(excinfo.value)
    assert excinfo.value.obj == play._ds
    assert excinfo.value.orig_exc.args[0] == 'mocked error'
    mock_load_list_of_blocks.assert_called_once_with(ds=play._ds, play=play, variable_manager=play._variable_manager, loader=play._loader)
