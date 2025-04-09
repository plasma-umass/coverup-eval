# file lib/ansible/playbook/play.py:121-131
# lines [121, 123, 124, 126, 127, 129, 131]
# branches ['123->124', '123->126', '126->127', '126->129']

import pytest
from unittest.mock import patch

# Assuming the Play class is imported from ansible.playbook.play
from ansible.playbook.play import Play

@pytest.fixture
def play_instance():
    return Play()

def test_get_name_with_name(play_instance):
    play_instance.name = "Test Play"
    assert play_instance.get_name() == "Test Play"

def test_get_name_with_hosts_sequence(play_instance):
    play_instance.name = None
    play_instance.hosts = ["host1", "host2"]
    assert play_instance.get_name() == "host1,host2"

def test_get_name_with_single_host(play_instance):
    play_instance.name = None
    play_instance.hosts = "single_host"
    assert play_instance.get_name() == "single_host"

def test_get_name_with_no_hosts(play_instance):
    play_instance.name = None
    play_instance.hosts = None
    assert play_instance.get_name() == ""
