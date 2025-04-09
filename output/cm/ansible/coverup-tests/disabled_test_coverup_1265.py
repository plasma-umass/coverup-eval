# file lib/ansible/playbook/play.py:121-131
# lines [123, 124, 126, 127, 129, 131]
# branches ['123->124', '123->126', '126->127', '126->129']

import pytest
from ansible.playbook.play import Play

# Assuming the Play class is part of a larger module and has dependencies that need to be mocked
# The test below is designed to cover lines 123-131 of the Play class

@pytest.fixture
def mock_play(mocker):
    # Mocking the Base and Taggable classes that Play inherits from
    mocker.patch('ansible.playbook.play.Base')
    mocker.patch('ansible.playbook.play.Taggable')
    mocker.patch('ansible.playbook.play.CollectionSearch')
    return Play()

def test_play_get_name_with_name_set(mock_play):
    # Set the name attribute directly to test the condition on line 123
    mock_play.name = 'test_play'
    assert mock_play.get_name() == 'test_play'

def test_play_get_name_with_hosts_as_sequence(mock_play):
    # Set the hosts attribute to a sequence to test the condition on line 126
    mock_play.hosts = ['host1', 'host2']
    assert mock_play.get_name() == 'host1,host2'

def test_play_get_name_with_hosts_as_string(mock_play):
    # Set the hosts attribute to a string to test the condition on line 129
    mock_play.hosts = 'all'
    assert mock_play.get_name() == 'all'

def test_play_get_name_with_hosts_as_none(mock_play):
    # Set the hosts attribute to None to test the condition on line 129
    mock_play.hosts = None
    assert mock_play.get_name() == ''
