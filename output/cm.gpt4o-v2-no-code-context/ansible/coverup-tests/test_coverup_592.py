# file: lib/ansible/playbook/play.py:183-191
# asked: {"lines": [183, 188, 189, 190, 191], "branches": []}
# gained: {"lines": [183, 188, 189, 190, 191], "branches": []}

import pytest
from ansible.playbook.play import Play
from ansible.errors import AnsibleParserError
from unittest.mock import patch, MagicMock

@pytest.fixture
def play_instance():
    play = Play()
    play._variable_manager = MagicMock()
    play._loader = MagicMock()
    play._ds = MagicMock()
    return play

def test_load_post_tasks_success(play_instance, monkeypatch):
    mock_load_list_of_blocks = MagicMock(return_value='mocked_blocks')
    monkeypatch.setattr('ansible.playbook.play.load_list_of_blocks', mock_load_list_of_blocks)
    
    ds = [{'some': 'data'}]
    result = play_instance._load_post_tasks('post_tasks', ds)
    
    mock_load_list_of_blocks.assert_called_once_with(ds=ds, play=play_instance, variable_manager=play_instance._variable_manager, loader=play_instance._loader)
    assert result == 'mocked_blocks'

def test_load_post_tasks_failure(play_instance, monkeypatch):
    def mock_load_list_of_blocks(ds, play, variable_manager, loader):
        raise AssertionError("mocked error")
    
    monkeypatch.setattr('ansible.playbook.play.load_list_of_blocks', mock_load_list_of_blocks)
    
    ds = [{'some': 'data'}]
    
    with pytest.raises(AnsibleParserError) as excinfo:
        play_instance._load_post_tasks('post_tasks', ds)
    
    assert "A malformed block was encountered while loading post_tasks" in str(excinfo.value)
    assert excinfo.value.obj == play_instance._ds
    assert isinstance(excinfo.value.orig_exc, AssertionError)
