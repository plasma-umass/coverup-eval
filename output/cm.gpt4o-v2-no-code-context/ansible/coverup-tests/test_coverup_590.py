# file: lib/ansible/playbook/play.py:163-171
# asked: {"lines": [163, 168, 169, 170, 171], "branches": []}
# gained: {"lines": [163, 168, 169, 170, 171], "branches": []}

import pytest
from ansible.playbook.play import Play
from ansible.errors import AnsibleParserError
from ansible.utils.display import Display
from unittest.mock import patch, MagicMock

@pytest.fixture
def play_instance():
    play = Play()
    play._variable_manager = MagicMock()
    play._loader = MagicMock()
    play._ds = MagicMock()
    return play

def test_load_tasks_success(play_instance, monkeypatch):
    mock_load_list_of_blocks = MagicMock(return_value='mocked_blocks')
    monkeypatch.setattr('ansible.playbook.play.load_list_of_blocks', mock_load_list_of_blocks)
    
    result = play_instance._load_tasks('attr', 'ds')
    
    mock_load_list_of_blocks.assert_called_once_with(ds='ds', play=play_instance, variable_manager=play_instance._variable_manager, loader=play_instance._loader)
    assert result == 'mocked_blocks'

def test_load_tasks_failure(play_instance, monkeypatch):
    def mock_load_list_of_blocks(*args, **kwargs):
        raise AssertionError("mocked error")
    
    monkeypatch.setattr('ansible.playbook.play.load_list_of_blocks', mock_load_list_of_blocks)
    
    with pytest.raises(AnsibleParserError) as excinfo:
        play_instance._load_tasks('attr', 'ds')
    
    assert "A malformed block was encountered while loading tasks: mocked error" in str(excinfo.value)
