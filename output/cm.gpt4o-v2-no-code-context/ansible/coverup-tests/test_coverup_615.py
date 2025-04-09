# file: lib/ansible/playbook/play.py:173-181
# asked: {"lines": [173, 178, 179, 180, 181], "branches": []}
# gained: {"lines": [173, 178, 179, 180, 181], "branches": []}

import pytest
from ansible.playbook.play import Play
from ansible.errors import AnsibleParserError
from unittest.mock import Mock, patch

@pytest.fixture
def play_instance():
    play = Play()
    play._variable_manager = Mock()
    play._loader = Mock()
    play._ds = Mock()
    return play

def test_load_pre_tasks_success(play_instance, monkeypatch):
    mock_load_list_of_blocks = Mock(return_value='expected_result')
    monkeypatch.setattr('ansible.playbook.play.load_list_of_blocks', mock_load_list_of_blocks)
    
    ds = [{'name': 'task1'}, {'name': 'task2'}]
    result = play_instance._load_pre_tasks('pre_tasks', ds)
    
    mock_load_list_of_blocks.assert_called_once_with(ds=ds, play=play_instance, variable_manager=play_instance._variable_manager, loader=play_instance._loader)
    assert result == 'expected_result'

def test_load_pre_tasks_failure(play_instance, monkeypatch):
    def mock_load_list_of_blocks(ds, play, variable_manager, loader):
        raise AssertionError("mocked error")
    
    monkeypatch.setattr('ansible.playbook.play.load_list_of_blocks', mock_load_list_of_blocks)
    
    ds = [{'name': 'task1'}, {'name': 'task2'}]
    
    with pytest.raises(AnsibleParserError) as excinfo:
        play_instance._load_pre_tasks('pre_tasks', ds)
    
    assert "A malformed block was encountered while loading pre_tasks" in str(excinfo.value)
    assert excinfo.value.obj == play_instance._ds
    assert isinstance(excinfo.value.orig_exc, AssertionError)
