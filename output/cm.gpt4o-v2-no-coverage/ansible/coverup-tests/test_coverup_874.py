# file: lib/ansible/playbook/play.py:101-102
# asked: {"lines": [101, 102], "branches": []}
# gained: {"lines": [101, 102], "branches": []}

import pytest
from ansible.playbook.play import Play

@pytest.fixture
def play_instance():
    return Play()

def test_repr_calls_get_name(play_instance, mocker):
    mock_get_name = mocker.patch.object(play_instance, 'get_name', return_value='test_name')
    result = repr(play_instance)
    mock_get_name.assert_called_once()
    assert result == 'test_name'

def test_get_name_with_name(play_instance):
    play_instance.name = 'test_name'
    result = play_instance.get_name()
    assert result == 'test_name'

def test_get_name_with_hosts_sequence(play_instance):
    play_instance.name = None
    play_instance.hosts = ['host1', 'host2']
    result = play_instance.get_name()
    assert result == 'host1,host2'

def test_get_name_with_hosts_string(play_instance):
    play_instance.name = None
    play_instance.hosts = 'host1'
    result = play_instance.get_name()
    assert result == 'host1'

def test_get_name_with_no_name_or_hosts(play_instance):
    play_instance.name = None
    play_instance.hosts = None
    result = play_instance.get_name()
    assert result == ''
