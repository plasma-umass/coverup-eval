# file: lib/ansible/playbook/play.py:121-131
# asked: {"lines": [121, 123, 124, 126, 127, 129, 131], "branches": [[123, 124], [123, 126], [126, 127], [126, 129]]}
# gained: {"lines": [121, 123, 124, 126, 127, 129, 131], "branches": [[123, 124], [123, 126], [126, 127], [126, 129]]}

import pytest
from ansible.playbook.play import Play
from ansible.module_utils.common.collections import is_sequence

@pytest.fixture
def play_instance():
    return Play()

def test_get_name_with_name(play_instance):
    play_instance.name = "Test Play"
    assert play_instance.get_name() == "Test Play"

def test_get_name_with_sequence_hosts(play_instance, mocker):
    play_instance.name = None
    play_instance.hosts = ["host1", "host2"]
    mocker.patch("ansible.module_utils.common.collections.is_sequence", return_value=True)
    assert play_instance.get_name() == "host1,host2"

def test_get_name_with_non_sequence_hosts(play_instance, mocker):
    play_instance.name = None
    play_instance.hosts = "host1"
    mocker.patch("ansible.module_utils.common.collections.is_sequence", return_value=False)
    assert play_instance.get_name() == "host1"

def test_get_name_with_empty_hosts(play_instance, mocker):
    play_instance.name = None
    play_instance.hosts = None
    mocker.patch("ansible.module_utils.common.collections.is_sequence", return_value=False)
    assert play_instance.get_name() == ""
